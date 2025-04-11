# SportHub Bot
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

Telegram-бот для проекта SportHub

## Возможности:
- [x] позволяет входить в учётную запись SportHub
- [x] служит одним из способов получения уведомлений
- [ ] повторяет основные функции веб-приложения

## Стек:
- Python ^3.12 — язык программирования
- [KurimuzonAkuma / pyrogram](https://github.com/KurimuzonAkuma/pyrogram/) 2.1.31 — фреймворк для работы с Telegram MTProto API
- [uvloop](https://github.com/MagicStack/uvloop/) ^0.21.0 — более быстрый цикл событий, чем стандартный asyncio
- [TgCrypto](https://github.com/pyrogram/tgcrypto) ^1.2.5 — библиотека криптографии для Telegram, более быстрая, чем стандартная
- [FastAPI](https://fastapi.tiangolo.com/) ^0.115.5 — веб-фреймворк для Python
- [uvicorn](https://www.uvicorn.org/) ^0.32.1 — ASGI сервер
- [Ruff](https://github.com/astral-sh/ruff) 0.7.1 — инструмент для форматирования и анализа кода

## Установка и запуск

### Посредством Docker

1. Установите и настройте [Docker](https://www.docker.com/), как указано в документации.
2. Из папки проекта выполните команду:
```shell
docker build -t sporthub-bot .
```
3. Теперь запускать бота можно командой:
```shell
docker run -it -d sporthub-bot
```

### Без использования Docker

1. Установите [Poetry](https://python-poetry.org/) одним из способов, указанных в документации.
2. Выполните установку зависимостей:
```shell
poetry install
```
3. Создайте файл `.env` на основе `template.env` и присвойте переменным соответствующие значения. Если ваш тестовый бот создан не на [тестовых серверах Telegram](https://habr.com/ru/companies/selectel/articles/763286/), закомментируйте следующую строку в `src/main.py`:
```python
test_mode=test_mode,
```
4. Теперь запускать бота можно командой:
```shell
poetry run python src.main
```

