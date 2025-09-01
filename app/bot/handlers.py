import asyncio
import logging

from aiogram import Router

from app.bot.formatter import format_commit_message
from app.config import config
from app.tracker.github import GitHubTracker

router = Router()
tracker = GitHubTracker()
logger = logging.getLogger(__name__)


async def send_notification(bot, update_info):
    message = format_commit_message(update_info)
    await bot.send_message(
        chat_id=config.CHAT_ID,
        text=message
    )
    logger.info(
        f"New commit notification sent: {update_info['commit']['sha'][:8]} - Layer {update_info['layer_number']}")


async def start_tracking(bot):
    logger.info(f"GitHub commit tracker started - checking every {config.CHECK_INTERVAL} seconds")

    # await bot.send_message(
    #     chat_id=config.CHAT_ID,
    #     text=(
    #         "🤖 <b>MTProto Layer Tracker Started!</b>\n\n"
    #         "Monitoring api.tl for updates...\n\n"
    #         "@MTProtoUpdates • <a href='https://github.com/bohd4nx/MTProto-Crawler'>View on GitHub</a>"
    #     )
    # )

    while True:
        try:
            updates = tracker.check_for_updates()
            for update_info in updates:
                await send_notification(bot, update_info)
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            logger.info("Tracking task cancelled")
            break
        except Exception as e:
            logger.error(f"Error during tracking: {str(e)}")
            try:
                await bot.send_message(
                    chat_id=config.CHAT_ID,
                    text=f"❌ Error:\n\n<code>{str(e)}</code>"
                )
            except Exception as send_error:
                logger.error(f"Failed to send error message: {send_error}")

        try:
            await asyncio.sleep(config.CHECK_INTERVAL)
        except asyncio.CancelledError:
            logger.info("Tracking task cancelled during sleep")
            break
