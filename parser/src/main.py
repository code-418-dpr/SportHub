import os
import logging
from pathlib import Path
from fastapi import FastAPI, Response, status
from dotenv import load_dotenv

from .process import process

OUTPUT_PATH = Path('tmp/table.pdf')

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    filemode='w',
    format='%(name)s %(asctime)s %(levelname)s %(message)s',
)

app = FastAPI()

@app.post("/run-parser")
async def run_parser(response: Response) -> Response:
    try:
        result = await process(os.getenv('LOCAL_PDF_ONLY'))
    except:
        logger.critical('Непредусмотренная ошибка')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK if result else status.HTTP_400_BAD_REQUEST
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3001)
