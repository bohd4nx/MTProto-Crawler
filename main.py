import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers import router as main_router, start_tracking
from app.bot.start import router as start_router
from app.config import config

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(levelname)s: %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)

for logger_name in ['aiogram.dispatcher', 'aiogram.events']:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML", link_preview_is_disabled=True))
dp = Dispatcher()
dp.include_router(main_router)
dp.include_router(start_router)


async def main():
    tracking_task = start_tracking(bot)
    polling_task = dp.start_polling(bot, skip_updates=True)

    try:
        await asyncio.gather(tracking_task, polling_task)
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
