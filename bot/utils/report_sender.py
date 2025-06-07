from aiogram.types import Message, FSInputFile
import shutil
from pathlib import Path

HTML_DIR = Path("reports/html")
ZIP_PATH = Path("reports/last_report.zip")

async def send_last_report(message: Message):
    if not HTML_DIR.exists():
        await message.answer("❌ Отчет не найден. Сначала запусти /run_tests")
        return

    # Архивируем HTML отчет
    shutil.make_archive(ZIP_PATH.with_suffix(""), 'zip', root_dir=HTML_DIR)

    await message.answer("📎 Отправляю последний отчет:")
    await message.answer_document(FSInputFile(ZIP_PATH))
