from .base import *

DEBUG = False

ADMINS = (
    ('tima', 'timur.dootaliev.td@gmail.com'),
)

ALLOWED_HOSTS = ['www.educa-tutorial.com', 'educa-tutorial.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educadb',
        'USER': 'timur',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}