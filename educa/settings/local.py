from .base import *

DEBUG = True
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
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