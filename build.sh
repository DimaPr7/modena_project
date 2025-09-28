#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt

# Сбор статики и миграции
python manage.py collectstatic --noinput
python manage.py migrate
