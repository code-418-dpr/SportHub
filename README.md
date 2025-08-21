# SportHub

[![license](https://img.shields.io/github/license/code-418-dpr/SportHub)](https://opensource.org/licenses/MIT)
[![release](https://img.shields.io/github/v/release/code-418-dpr/SportHub?include_prereleases)](https://github.com/code-418-dpr/SportHub/releases)

Агрегатор обновлений единого календарного плана спортивных мероприятий Министерства спорта России

<details>
  <summary><h2>Демо</h2></summary>
  <img width="70%" src="https://github.com/user-attachments/assets/b965bd53-e269-46e1-a39a-96e7c7254379" />
  <img width="70%" src="https://github.com/user-attachments/assets/dd8bc1c7-9b7c-463f-ad2f-7afec08fbbd1" />
  <img width="70%" src="https://github.com/user-attachments/assets/b23d7340-da67-4240-bf8a-c70b2ce1fe01" />
  <img width="70%" src="https://github.com/user-attachments/assets/d1ed5f12-133a-442f-9e91-c6e11ca572b3" />
  <img width="70%" src="https://github.com/user-attachments/assets/8fa044af-b290-49ae-9f64-899f4a1344f3" />
  <img width="70%" src="https://github.com/user-attachments/assets/d1710888-7e8f-4485-9a9d-4b07ab9c0ef7" />
  <img width="70%" src="https://github.com/user-attachments/assets/7c4df366-b387-479e-9649-96726b87d7cf" />
  <img width="70%" src="https://github.com/user-attachments/assets/d399a959-d432-4785-b68f-da01cb0cc54c" />
  <img width="70%" src="https://github.com/user-attachments/assets/dbdb0f4c-2604-4ad1-ab09-77963648fe9f" />
  <img width="70%" src="https://github.com/user-attachments/assets/9209420f-468e-44ac-b5ea-c543a7d42084" />
  <img width="70%" src="https://github.com/user-attachments/assets/fb5f3fd1-5b78-4151-a8bf-66147f7e1641" />
  <img width="70%" src="https://github.com/user-attachments/assets/088cb675-b994-4802-9447-837d03dc3c21" />
  <img width="70%" src="https://github.com/user-attachments/assets/086b72b4-4f83-461e-a1ac-44c663c8b1e0" />
  <img width="70%" src="https://github.com/user-attachments/assets/0440f2ba-66ac-4e21-819e-d8e9dd6e76fc" />
  <img width="70%" src="https://github.com/user-attachments/assets/8c1a76cc-2f6a-4763-b206-c0e923ee2373" />
  <img width="70%" src="https://github.com/user-attachments/assets/925048b5-f5ef-4e3c-8444-c8284586a83c" />
  <img width="70%" src="https://github.com/user-attachments/assets/e79d7313-8f79-4c81-b797-e63e05366a9b" />
  <img width="70%" src="https://github.com/user-attachments/assets/b722ed4c-6d4f-4d54-bf9a-41544b0bd165" />
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
mv ./services/SportHub-notification-service/.env ./services/SportHub-notification-service/_.env 
docker compose --profile local up -d --build
mv ./services/SportHub-web/_.env ./services/SportHub-web/.env 
mv ./services/SportHub-parser/_.env ./services/SportHub-parser/.env
mv ./services/SportHub-notification-service/_.env ./services/SportHub-notification-service/.env
```
