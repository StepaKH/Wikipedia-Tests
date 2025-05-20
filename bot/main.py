import sys
from pathlib import Path

from bot.utils.scheduler import start_scheduler

sys.path.append(str(Path(__file__).parent.parent))

from aiogram import Bot, Dispatcher
import asyncio
from bot.handlers.commands import router
from bot.config import BOT_TOKEN

bot_tg = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def on_startup(_):
    print("✅ Бот запущен и готов к работе")

async def main():
    await on_startup(None)

    start_scheduler()

    await dp.start_polling(bot_tg, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())