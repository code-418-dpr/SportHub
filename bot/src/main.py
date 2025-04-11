import os
import sys
import logging
import threading

import pyrogram
import uvicorn
from fastapi import FastAPI, Response
from dotenv import dotenv_values

from . import handlers

logger = logging.getLogger(__name__)
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    filemode='w',
    format='%(name)s %(asctime)s %(levelname)s %(message)s',
)

env: dict[str, str | None] = dotenv_values()
backend_host = env['BACKEND_HOST']
backend_port = int(env['BACKEND_PORT'])
test_mode = bool(env['TEST_MODE_ENABLED'])
api_id = env['API_ID']
api_hash = env['API_HASH']
if test_mode:
    name = 'TestBot'
    bot_token = env['TEST_TOKEN']
else:
    name = 'Bot'
    bot_token = env['TOKEN']


if env['USE_UVLOOP'] and sys.platform != 'win32':
    logger.info('uvloop подключён')
    import uvloop
    uvloop.install()
else:
    logger.info('asyncio подключён')

bot = pyrogram.Client(
    f'../{name}',
    api_id,
    api_hash,
    lang_code='ru',
    bot_token=bot_token,
    test_mode=test_mode,
)
app = FastAPI()


from pydantic import BaseModel

from .utils.tg_auth import token_to_ids

BACKEND_URL = os.getenv('BACKEND_URL')

class MessageRequest(BaseModel):
    chat_id: int
    message: str


@app.post('/authorization/{token}')
async def authorization(token: str, response: Response) -> Response:
    try:
        user_id, msg_id = token_to_ids(token)
        await bot.send_message(user_id, 'Авторизация прошла успешно!')
        await bot.delete_messages(user_id, msg_id)
    except:
        response.status_code = 400
        logging.exception('Ошибка при отправке сообщения')
    else:
        response.status_code = 200
    return response

@app.post('/send-message')
async def send_message(request: MessageRequest, response: Response) -> Response:
    try:
        await bot.send_message(request.chat_id, request.message)
    except:
        response.status_code = 400
        logging.exception('Ошибка при отправке сообщения')
    else:
        response.status_code = 200
    return response



def run_uvicorn() -> None:
    uvicorn.run(
        app, host=backend_host, port=backend_port, log_level='info', workers=1,
    )


if __name__ == '__main__':
    threading.Thread(target=run_uvicorn).start()

    bot.add_handler(handlers.start)
    bot.add_handler(handlers.help_)

    bot.run()
