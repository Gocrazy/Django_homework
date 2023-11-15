#!/bin/bash -x
echo 'Run migration'
python manage.py makemigrations
python manage.py migrate
exec "$@"
