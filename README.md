# Airbnb clone 2
- Review airbnb course of nomad coders for learning django framework more clearly

- I'll recap the course below

## Environment
- Touch gitignore(for python) & README.md
- Set up virtual env with pipenv & install django
- You should always execute commands in a virtual environment. 
- Execute the command in terminal: django-admin startproject config .
(best way to start django project)
- Install formatter:black & linter:flake8

## basic Django
- Execute the command for running django server: python manage.py runserver
- Create super user: python manage.py createsuperuser
- 'makemigrations' checks for changes on the data shape and creates a file describing the changes
- 'migrate' applies the migrations to the database 
- 'migrate' after 'makemigrations'

## Divide & Conquer
- In Django, 'project' is meant that group of 'applications'
& 'application' group of functions
- You should not put many functions in one application.
- You should divide project to many app because of modularization
- In Airbnb course, i'm going to make the app like this: User, Rooms, List, Reservations, Reviews, Conversation
- Tips for dividing app: When you explain the app, only one sentence. must not contain 'AND'. for example "rooms display, update, create, delete AND list edit, update..."

## App
- Create app with this command: django-admin startapp 'app_name'
- App's name should be plural like 'rooms'
- Name of files in app that you created should be same to first
- Don't change app & file name. Observe the django rules.
- You should not delete existing files in app. but you can add files in app like urls.py
