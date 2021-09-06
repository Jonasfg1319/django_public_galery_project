# public_galery_fullstack_django
public gallery project using Django framework

This is a project from a public gallery developed using django framework

## Tecnologies

- Django
- Html
- Css
- Javascript

## How to run the project?

You must have installed on your machine:

```
Python 3.7.4
Django 3.2.5
```

Download the project and go to public_gallery/settings.py

In settings.py look for database configure the database of your choice, in mysql

```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


```
start your database.

After that, open your terminal and navigate to the project root

run the following command

```
python manage.py migrate
```

this command will create all the tables needed to run the application in your database

then start the application

```
python manage.py runserver 
```

the application will start on your localhost


