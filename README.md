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

'rest_framework'
'rest_framework.authtoken'
'profiles_api'
