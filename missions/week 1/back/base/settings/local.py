from .common import *

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ably',
        'USER':'kjkim',
        'PASSWORD':'kj123!@#',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS': {
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}