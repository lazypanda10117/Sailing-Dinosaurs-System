#!/usr/bin/env bash
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
