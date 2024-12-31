"""
DJANGO COMMANDS

djando-admin help                           -> list of commands
django-admin startproject project_name      -> create a new project

python manage.py runserver                   -> start the server
python manage.py startapp app_name           -> create a new app

after creating a new app, add it to the INSTALLED_APPS in settings.py
to add the app to the project:
    'app_name.apps.AppNameConfig', -> add this to the INSTALLED_APPS in settings.py

python manage.py migrate            -> apply the migration

python manage.py createsuperuser    -> create a superuser

django.contrib.humanize             -> to use humanize in the templates
{% load humanize %}                 -> to load humanize in the template
https://docs.djangoproject.com/en/5.1/ref/contrib/humanize/



"""


import django
