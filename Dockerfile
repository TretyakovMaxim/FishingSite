# Базовый образ с Python
FROM python:3.11.3

# Установка зависимостей
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копирование приложения в контейнер
COPY ./fishing /code/

# Запуск миграций и запуск сервера Django
RUN python manage.py migrate

# Открытие порта для веб-сервера Django
EXPOSE 8000

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]