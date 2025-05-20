from types import SimpleNamespace

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from bot.config import ADMIN_ID
from bot.utils.report_sender import send_last_report
from bot.utils.test_runner import run_tests, is_tests_running

scheduler = AsyncIOScheduler()

def start_scheduler():
    if not scheduler.running:
        scheduler.start()

def schedule_tests(bot: Bot, hour: int, minute: int):
    scheduler.add_job(
        run_scheduled_tests,
        CronTrigger(hour=hour, minute=minute),
        args=[bot],
        id="scheduled_test",
        replace_existing=True
    )

def cancel_scheduled_tests():
    scheduler.remove_job("scheduled_test")

def is_schedule_active() -> bool:
    return scheduler.get_job("scheduled_test") is not None

class FakeMessage:
    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat = SimpleNamespace(id=chat_id)
        self.from_user = SimpleNamespace(id=chat_id)

    async def answer(self, text: str, **kwargs):
        await self.bot.send_message(self.chat.id, text, **kwargs)

    async def answer_document(self, document, **kwargs):
        await self.bot.send_document(self.chat.id, document, **kwargs)

async def run_scheduled_tests(bot: Bot):
    if is_tests_running():
        return

    result_msg, _, errors_summary, _ = await run_tests()

    await bot.send_message(ADMIN_ID, "🕒 Автоматический запуск по расписанию")
    await bot.send_message(ADMIN_ID, result_msg)

    if errors_summary:
        await bot.send_message(ADMIN_ID, "⚠️ Упавшие тесты:\n" + errors_summary)

    fake_message = FakeMessage(bot, ADMIN_ID)
    await send_last_report(fake_message)