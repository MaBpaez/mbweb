#!/bin/bash
echo GOOGLE_APPLICATION_CREDENTIALS_JSON > /app/credentials.json
python manage.py migrate
gunicorn mbsocialweb.wsgi
