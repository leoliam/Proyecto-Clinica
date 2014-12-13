from .base  import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddgo4sr10ncac0',
        'USER': 'reaoqihqndirvh',
        'PASSWORD': 'M8uq01hs52NroNpeVT1_KPY2oN',
        'HOST' : 'ec2-54-163-255-191.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'