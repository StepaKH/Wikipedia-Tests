import re

import httpx
from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import ADMIN_ID
from bot.keyboards.main_menu import get_main_menu
from bot.utils.report_sender import send_last_report
from bot.utils.scheduler import schedule_tests, is_schedule_active, cancel_scheduled_tests
from bot.utils.test_runner import run_tests, stop_tests, is_tests_running

ALLOWED_MARKERS = ["smoke", "negative", "onboarding", "positive", "auth", "registration", "validation", "customize_feed", "customize_random", "article", "tabs", "search", "saved"]
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Доступ запрещен")
        return

    keyboard = get_main_menu()
    await message.answer("✅ Бот работает!\nВыберите действие:", reply_markup=keyboard)

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "🛠 *Команды бота:*\n\n"
        "📌 /start — Приветствие\n"
        "🚀 /run_tests [кол-во] [маркер] — Запуск тестов\n"
        "🛑 /stop_tests — Остановить тесты\n"
        "📄 /last_report — Получить последний отчёт\n"
        "🏷 /markers — Список допустимых маркеров\n"
        "⏰ /schedule_tests HH:MM — Ежедневный автозапуск\n"
        "❌ /cancel_schedule — Отключить автозапуск\n"
        "🔁 /simulate_push — Имитация push в GitHub\n"
        "ℹ️ /help — Показать это сообщение"
    )
    keyboard = get_main_menu()
    await message.answer(help_text, parse_mode="Markdown", reply_markup=keyboard)

def format_resource_stats(stats: dict) -> str:
    return (
        "📊 Ресурсы системы:\n"
        f"⏱ Длительность: {stats['duration']} сек\n"
        f"🖥 CPU: {stats['cpu']}% ({stats['cpu_diff']:+}%)\n"
        f"🧠 RAM: {stats['ram']}% ({stats['ram_diff']:+}%)"
    )

@router.message(Command("run_tests"))
@router.message(Command("run_tests"))
async def handle_run_tests(message: Message):
    if is_tests_running():
        await message.answer("⚠️ Тесты уже запущены. Пожалуйста, дождитесь завершения.")
        return

    args = message.text.strip().split()
    try:
        count = int(args[1]) if len(args) > 1 else 1
        if count < 1 or count > 10:
            raise ValueError
    except ValueError:
        await message.answer("❌ Укажи число от 1 до 10, например:\n/run_tests 2", parse_mode="Markdown")
        return

    marker = args[2] if len(args) > 2 else None
    if marker and marker not in ALLOWED_MARKERS:
        await message.answer(
            "❌ Неверный маркер. Допустимые:\n" + "\n".join(f"• {m}" for m in ALLOWED_MARKERS),
            parse_mode="Markdown"
        )
        return

    msg = f"🚀 Запускаю тесты на *{count}* поток(а/ов)"
    if marker:
        msg += f" с маркером *{marker}*"
    await message.answer(msg + "...", parse_mode="Markdown")

    result_msg, success, errors_summary, resource_stats = await run_tests(
        parallel_count=count,
        marker=marker
    )

    await message.answer(result_msg)
    await message.answer(format_resource_stats(resource_stats))

    if errors_summary:
        await message.answer("⚠️ Найдены упавшие тесты:\n" + errors_summary)

    await send_last_report(message)

@router.message(Command("stop_tests"))
async def cmd_stop_tests(message: types.Message):
    was_stopped = await stop_tests()
    if was_stopped:
        await message.answer("🛑 Тесты были остановлены вручную.")
    else:
        await message.answer("ℹ️ Тесты не запущены или уже завершены.")

@router.message(Command("last_report"))
async def cmd_last_report(message: types.Message):
    await send_last_report(message)

@router.message(Command("markers"))
async def cmd_markers(message: Message):
    if not ALLOWED_MARKERS:
        await message.answer("⚠️ Нет доступных маркеров.")
        return

    formatted = "\n".join([f"• {m}" for m in ALLOWED_MARKERS])
    await message.answer("🏷 Доступные маркеры:\n" + formatted, parse_mode="Markdown")

@router.message(Command("simulate_push"))
async def simulate_push(message: Message):
    async with httpx.AsyncClient() as client:
        commit = await client.post(
            "http://localhost:8000/repos/fake_user/fake_repo/git/commits",
            json={"message": "Тестовый коммит из Telegram"}
        )

        webhook = await client.post(
            "http://localhost:8000/api/webhook",
            headers={"X-GitHub-Event": "push"},
            json={
                "ref": "refs/heads/main",
                "commits": [commit.json()]
            }
        )

    await message.answer(
        "🔁 Имитация GitHub flow:\n"
        f"1. Создан коммит: {commit.json()['sha']}\n"
        f"2. Вебхук статус: {webhook.json()['status']}\n\n"
        "Запускаю тесты..."
    )
    await handle_run_tests(message)

@router.message(Command("schedule_tests"))
async def cmd_schedule_tests(message: Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Доступ запрещен")
        return

    args = message.text.strip().split()
    if len(args) != 2 or not re.match(r"^\d{2}:\d{2}$", args[1]):
        await message.answer("❌ Укажи время в формате HH:MM, например:\n/schedule_tests 22:30")
        return

    hour, minute = map(int, args[1].split(":"))
    if not (0 <= hour < 24 and 0 <= minute < 60):
        await message.answer("❌ Недопустимое время. Пример: /schedule_tests 08:15")
        return

    schedule_tests(bot, hour, minute)
    await message.answer(f"✅ Тесты будут запускаться ежедневно в {hour:02d}:{minute:02d}")

@router.message(Command("cancel_schedule"))
async def cmd_cancel_schedule(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Доступ запрещен")
        return

    if is_schedule_active():
        cancel_scheduled_tests()
        await message.answer("❌ Автоматический запуск отключён.")
    else:
        await message.answer("ℹ️ Расписание не установлено.")
