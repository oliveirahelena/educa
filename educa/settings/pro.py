from .base import *

DEBUG = False

ADMINS = (
    ('Codey Bot', 'codey@gmail.com'),
)

ALLOWED_HOSTS = ['host.docker.internal']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'HOST': 'localhost',
       'NAME': 'educa',
       'USER': 'postgres',
       'PASSWORD': 'postgres'
   }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True