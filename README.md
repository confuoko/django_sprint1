# Blogicum
# Описание.

## Проект django_sprint1.

## Технологии:
* Python 3.7
* Django 3.2

## Описание проекта

Небольшая социальная сеть для публикации личных дневников. Данные для социальной сети располагаются списком в файле views.py.

## Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:

        git clone git@github.com:RiSSoL-86/django_sprint1.git
        cd django_sprint1

* Cоздать и активировать виртуальное окружение:

        python -m venv venv
        source venv/Scripts/activate

* Установить зависимости из файла requirements.txt:

        python -m pip install --upgrade pip
        pip install -r requirements.txt

* Запустить проект:

        python manage.py runserver

* Перейти на локальный сервер:

        http://127.0.0.1:8000/
