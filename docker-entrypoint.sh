#!/bin/bash

python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput
python manage.py migrate

exec gunicorn kquiz.wsgi:application -w 2 -b :8000
