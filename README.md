### API-проект для сайта-блоггинга YATUBE:

Это проект YATUBE без фронтенд-части (чистый бэкенд).

Благодаря этому коду вы сможете работать с платформой YATUBE через API-запросы!
Преимущество данного проекта в том, что вы можете оформить фронтенд YATUBE (например через React) и подключить к нему бэкенд-приложение из этого проекта!

В проекте предусмотрена защита данных через JWT-токены!

### Примеры API-запросов:

```
РАБОТА С ПОСТАМИ:


/api/v1/posts/


Доступны GET и POST запросы.

GET-запрос на данный эндпойнт позволит вам получить список (list) всех постов пользователей.

POST-запрос на данный эндпойнт позволит вам (в качестве авторизованного пользователя платформы) создать пост.


/api/v1/posts/{id}/


Доступны GET, PUT, PATCH и DELETE запросы.

GET-запрос на данный эндпойнт позволит вам получить определенный пост из базы данных проекта.

PUT-запрос и PATCH-запрос на данный эндпойнт позволят вам изменить или частично изменить собственный пост.

DELETE-запрос позволит вам удалить собственный пост.
```

```
РАБОТА С ГРУППАМИ:


Доступны GET запросы.


/api/v1/groups/ - сделанный запрос на данный эндпойнт вернет вам список (list) всех групп проекта.


/api/v1/groups/{id}/ - сделанный запрос на данный эндпойнт вернет вам конкретную группу.
```

```
РАБОТА С КОММЕНТАРИЯМИ:


/api/v1/posts/{post_id}/comments/


Доступны GET и POST запросы.

GET-запрос на данный эндпойнт позволит вам получить список (list) всех комментариев конкретного поста.

POST-запрос на данный эндпойнт позволит вам (в качестве авторизованного пользователя платформы) оставить комментарий к конкретному посту.


/api/v1/posts/{post_id}/comments/{id}/


Доступны GET, PUT, PATCH и DELETE запросы.

GET-запрос на данный эндпойнт позволит вам получить конкретный комментарий к определенному посту.

PUT-запрос и PATCH-запрос на данный эндпойнт позволят вам изменить или частично изменить собственный комментарий.

DELETE-запрос позволит вам удалить собственный комментарий.
```

```
РАБОТА С ПОДПИСКАМИ:


/api/v1/follows/


Доступны GET и POST запросы.

GET-запрос на данный эндпойнт позволит вам (в качестве авторизованного пользователя платформы) получить список (list) всех ваших подписок на авторов постов.

POST-запрос на данный эндпойнт позволит вам (в качестве авторизованного пользователя платформы) подписаться на конкретного автора поста\ов.
```

Документация с примерами запросов, кодами ответов доступна тут: http://127.0.0.1:8000/redoc/ (после активации проекта)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AllanKudi/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```