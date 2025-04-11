import logging
from pathlib import Path
import httpx
import aiofiles

logger = logging.getLogger(__name__)
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    filemode='w',
    format='%(name)s %(asctime)s %(levelname)s %(message)s',
)


async def download_file(http_client: httpx.AsyncClient, path: Path, url: str) -> bool:
    logger.info('Скачиваем файл по адресу %s', url)

    try:
        async with (
            http_client.stream('GET', url) as response,
            aiofiles.open(path, 'wb') as file,
        ):
            async for chunk in response.aiter_bytes():
                await file.write(chunk)
    except Exception:
        logger.exception('Ошибка при скачивании файла')
        return False
    else:
        logger.info('Файл скачан')
        return True
