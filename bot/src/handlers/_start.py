import os

from dotenv import load_dotenv
from pyrogram import types

from ..utils.tg_auth import ids_to_token

load_dotenv()

BACKEND_URL = os.getenv('WEB_URL')


async def _start_handler_callback(_, msg: types.Message) -> None:
    token = ids_to_token(msg.from_user.id, msg.id)
    await msg.reply(
        'Физкульт-привет! 👋🏻\nАвторизуйтесь на сайте, чтобы воспользоваться ботом. 👇🏻',
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🏃🏻‍➡️ Авторизоваться', url=f'{BACKEND_URL}tg-auth/{token}')]
        ]))
