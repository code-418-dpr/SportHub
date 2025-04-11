# SportHub Parser
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

Парсер PDF-файла для проекта SportHub

## Возможности:
- [x] максимально точно распознаёт содержание PDF-файла
- [x] проверяет актуальность файла по указанию планировщика
- [x] готов к изменению ссылки на файл на странице Минспорта

## Стек:
- Python ^3.12 — язык программирования
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) ^1.24.14 — высокопроизводительный парсер PDF
- [Httpx](https://github.com/encode/httpx) ^0.27.2 — библиотека для отправки HTTP-запросов
- [FastAPI](https://github.com/fastapi/fastapi) ^0.115.5 — веб-фреймворк для приёма HTTP-запросов
- [uvicorn](https://github.com/encode/uvicorn) ^0.32.1 — ASGI сервер для FastAPI
- [Ruff](https://github.com/astral-sh/ruff) 0.7.1 — инструмент для форматирования и анализа кода

## Установка и запуск

### Посредством Docker

1. Установите и настройте [Docker](https://www.docker.com/), как указано в документации.
2. Из папки проекта выполните команду:
```shell
docker build -t sporthub-parser .
```
3. Теперь запускать сервер парсера можно командой:
```shell
docker run -it -d sporthub-parser
```

### Без использования Docker

1. Установите [Poetry](https://python-poetry.org/) одним из способов, указанных в документации.
2. Выполните установку зависимостей:
```shell
poetry install
```
3. Создайте файл `.env` на основе `template.env` и присвойте переменным соответствующие значения.
4. Теперь запустить сервер парсера можно командой:
```shell
poetry run python -m src.main
```
