from settings.local import *  # noqa

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'test37',
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}