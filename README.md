# SportHub

[![license](https://img.shields.io/github/license/code-418-dpr/SportHub)](https://opensource.org/licenses/MIT)
[![release](https://img.shields.io/github/v/release/code-418-dpr/SportHub?include_prereleases)](https://github.com/code-418-dpr/SportHub/releases)

Агрегатор обновлений единого календарного плана спортивных мероприятий Министерства спорта России

<details>
  <summary><h2>Демо</h2></summary>
   Здесь будут скриншоты, возможно даже видео.
</details>

## Особенности реализации

- веб-приложение
    - [x] хорошо смотрится как на десктопных, так и на мобильных устройствах
    - [x] позволяет просматривать список событий
    - [x] поддерживает все основные фильтры
    - [x] позволяет записываться и отменять запись на события
    - [x] позволяет добавлять события в Google Календарь
    - [x] поддерживает авторизацию пользователя, в том числе через аккаунт Яндекс
    - [x] получает от парсера наборы данных из обновлённого PDF и сопоставляет их с базой, попутно обновляя её
- парсер:
    - [x] точно распознаёт содержание PDF-файла
    - [x] проверяет актуальность файла по указанию планировщика
    - [x] готов к изменению ссылки на файл на странице Минспорта
- планировщик / сервис уведомлений:
    - [x] позволяет управлять частотой проверки обновлений PDF-файла
    - [x] отправляет необходимые уведомления пользователям в веб-приложение и на почту

## Архитектура

Проект состоит из микросервисов, предназначенных для развёртывания в Docker:

- [веб-приложение](https://github.com/code-418-dpr/SportHub-web)
- [парсер](https://github.com/code-418-dpr/SportHub-parser)
- [сервис уведомлений](https://github.com/code-418-dpr/SportHub-notification-service)
- Seq — система сбора логов и метрик
- PostgreSQL — база данных
- Traefik — обратный прокси

## В планах

- [ ] усовершенствовать систему рекомендаций, чтобы она учитывала больше персональных особенностей
- [ ] добавить возможность подключения уведомлений через Telegram-бота
- [ ] добавить больше вариантов просмотра календарного плана
- [ ] добавить карту предстоящих событий
- [ ] расширить спектр настроек уведомлений
- [ ] интегрировать Яндекс.Календарь и другие подобные сервисы

## Установка

> [!NOTE]
> Мы отказались от использования `git submodules` и `git subtree` из-за периодически возникающей путаницы при
> отслеживании изменений в монорепозиториях. Данный репозиторий представляет собой единую точку для работы с проектом,
> лишённую этих недостатков.

0. Клонируйте репозиторий и перейдите в его папку.
1. Клонируйте репозитории сервисов, входящих в состав проекта по SSH (рекомендуется):

```shell
git clone git@github.com:code-418-dpr/SportHub-web.git services/SportHub-web
git clone git@github.com:code-418-dpr/SportHub-parser.git services/SportHub-parser
git clone git@github.com:code-418-dpr/SportHub-notification-service.git services/SportHub-notification-service
```

или по HTTPS:

```shell
git clone https://github.com/code-418-dpr/SportHub-web.git services/SportHub-web
git clone https://github.com/code-418-dpr/SportHub-parser.git services/SportHub-parser
git clone https://github.com/code-418-dpr/SportHub-notification-service.git services/SportHub-notification-service
```

После этого вы можете вносить изменения в каждый из сервисов по-отдельности (в соответствии с инструкциями, описанными в
соответствующих README).

## Запуск и модификация

0. Установите проект по инструкции выше.
1. Создайте файл `.env` на основе [.env.template](.env.template) и задайте все указанные там параметры.
2. Установите Docker.
3. Теперь запускать проект **на сервере** можно командой:

```shell
docker compose --profile server up -d --build
```

При модификации сервисов проекта и их тестировании может потребоваться создание файлов .env для каждого из них. Однако,
при запуске всех сервисов в одном контейнере (из этого репозитория) их не должно быть. Чтобы не удалять их, для запуска
сервисов **на локальном устройстве** можно воспользоваться следующим набором команд:

```shell
mv ./services/SportHub-web/.env ./services/SportHub-web/_.env
mv ./services/SportHub-parser/.env ./services/SportHub-parser/_.env 
docker compose --profile local up -d --build
mv ./services/SportHub-web/_.env ./services/SportHub-web/.env 
mv ./services/SportHub-parser/_.env ./services/SportHub-parser/.env
```
