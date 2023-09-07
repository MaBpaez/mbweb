#!/bin/bash
python manage.py migrate
gunicorn mbsocialweb.wsgi
