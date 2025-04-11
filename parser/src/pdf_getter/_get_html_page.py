import logging
import httpx

logger = logging.getLogger(__name__)
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    filemode='w',
    format='%(name)s %(asctime)s %(levelname)s %(message)s',
)


async def get_html_page(client: httpx.AsyncClient, url: str) -> str | None:
    try:
        response = await client.get(url)
    except Exception:
        logger.exception('Ошибка при получении HTML-страницы сайта')
        return None
    else:
        logger.info('HTML-страница получена')
        return response.text
