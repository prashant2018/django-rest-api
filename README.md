# Django Rest Profile API

## Create Virtual Env

```bash
# Install virtualenv
sudo apt-get install python3-pip

sudo pip3 install virtualenv

# Create virtualenv
$ virtualenv venv

# Activate
$ source venv/bin/activate

#Deactivate
$ deactivate
```

## Install Dependencies

```bash
$ pip install -r requirements.txt
```

## Create Django Project

```bash
$ django-admin.py startproject profiles_project .
```

## Create Django App

```bash
$ python manage.py startapp profiles_api
```

## Adding apps in settings.py

#### Add these uner installed_apps:

rest_framework,
rest_framework.authtoken,
profiles_api

## Run Server

```bash
$ python manage.py runserver 0.0.0.0:8000
```

## Create Database

#### Create a model

#### Create a manager so custom model can be used from cli

Managers create function which can be used to create user etc

#### Configure project to use custom model for auth

In settings.py add at the end

```
AUTH_USER_MODEL = 'profiles_api.UserProfile'
```

## Django Migration

```bash
$ python manage.py makemigrations profiles_api
$ python manage.py migrate
```

## Create Superuser

```bash
$ python manage.py createsuperuser
```

## Register model in django admin panel

Inside admin.py of your app register the model

## APIViews

Handles incoming request
Add in views.py

## Serializer

Create serializers.py file under the app

## Viewsets

Create a Vieset just like APIViews in views.py

Viewsets offers list, create, update etc

Add the vieset into the routes using DefauoltRouter which provides url for list, update etc

## Permissions Class

Create permission.py file. In the viewset assign permission class created to 'permission_classes'

## Login API

import the following in views.py and add the class to handle login

```python
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authtoken"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

```

## Steps

1. Create a model
2. Add model to admin pannel
3. Create a serializer
4. Create Viewset
