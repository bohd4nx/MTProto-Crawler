from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config import config

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(format_status())
    return None


def format_status():
    tl_file_url = "https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/SourceFiles/mtproto/scheme/api.tl"

    return f"""🤖 <b>MTProto Layer Tracker Status</b>

📂 <b>Tracking:</b> <a href='{tl_file_url}'>api.tl</a> file changes
⏱ <b>Check interval:</b> {config.CHECK_INTERVAL} seconds

🔗 <a href='https://github.com/bohd4nx/MTProto-Crawler'>View on GitHub</a>"""
