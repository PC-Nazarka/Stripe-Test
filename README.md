# Stripe Test

[Built with Cookiecutter DjangoRestFramework](https://github.com/PC-Nazarka/cookiecutter-django-rest-framework/)

## Для запуска проекта

Создайте ```.env``` файл в корневой папке проекта со следующими переменными:
- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- STRIPE_SECRET_KEY
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

После создания файла запустите проект с помощью этих команд

```bash
docker-compose up --build -d
docker-compose run django python manage.py migrate
```

### Для создания супер пользователя

```bash
docker-compose exec django python manage.py createsuperuser
```

### Ссылка на административную панель

```http://0.0.0.0:8000/admin```

### Для удобства был написан скрипт для генерации данных

```bash
docker-compose run django python manage.py runscript fill_sample_data
```

### Выполненные бонусные задачи

- запуск, использую docker
- использование environment variables
- просмотр Django Моделей в Django Admin панели
