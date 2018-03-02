#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput

exec gunicorn kquiz.wsgi:application -w 2 -b :8000
