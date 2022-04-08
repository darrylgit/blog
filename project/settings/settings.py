from .base import *
import os


""" Turn off debug in production"""
DEBUG = True 
""" Turn off debug in production"""

# envrion variable should be look like APP_ALLOWED_HOSTS=192.168.1.133,192.168.1.131
# split method generates array
ALLOWED_HOSTS = os.environ.get('APP_ALLOWED_HOSTS', '127.0.0.1').split(',')

# Application definition add ons
INSTALLED_APPS+=[
    'taggit',
    #apps
    'apps.blog',
    'apps.casestudy',
    'apps.flatpage',
    'apps.project',
    'apps.media',
    'apps.mockup',
    'apps.writeup'
]

DATABASE_DEFAULT = {
    'default': {
        'ENGINE': os.environ.get('APP_BASE_ENGINE'),
        'NAME': os.environ.get('APP_BASE_NAME'),
        'USER': os.environ.get('APP_BASE_USER'),
        'PASSWORD': os.environ.get('APP_BASE_PASSWORD'),
        'HOST': os.environ.get('APP_BASE_HOST'),

        'TEST': {
            'NAME': os.environ.get('APP_BASE_TEST_NAME'),
        },
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

DATABASES = (
    DATABASE_DEFAULT
    if 'APP_BASE_HOST' in os.environ
    else {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
)