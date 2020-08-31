from .base import *

DEBUG = False

ADMINS = (
    ('Codey Bot', 'codey@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'HOST': 'localhost',
       'NAME': 'educa',
       'USER': 'postgres',
       'PASSWORD': 'postgres'
   }
}