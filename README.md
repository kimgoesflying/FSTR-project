# Django REST Framework with Swagger 
REST API [Базы по горным объектам России и СНГ](https://pereval.online/) для
Федерации Спортивного Туризма России (ФСТР).

## Задание
- Создан класс по работе с БД
- Путь к базе данных берётся из переменных окружения операционной системы: FSTR_DB_HOST, FSTR_DB_PORT, FSTR_LOGIN, FSTR_PASS 
- Реализован REST API
- Переработана структура базы данных
- Документация сделана с помощью Swagger
- Написана документация в Readme.md
- REST API опубликован на хостинге

## Старт
Требуется **Pythin 3+**, **Django 3+**, **PostgreSQL**

1. Установка
```
python -m pip install -r requirements
```
2. Рудактировать .env.example
```
cp .env.example .env
```
3. Применить миграции и запустить сервер
```
python manage.py migrate
python manage.py runserver
```
4. Тест
```
http://127.0.0.1:8000/api/v1/schema/swagger-ui
```
## DEMO
https://fstr-project.herokuapp.com/api/v1/schema/swagger-ui

https://fstr-project.herokuapp.com/admin

- user: root
- password: root
