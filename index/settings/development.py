from .base import *

DEBUG = True

# Define the database manager to setup the various projects
DATABASE_ROUTERS = ['core.database.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'threads_frontend_json_data': 'threads_json',
                         'comments_frontend_json_data': 'comments_json'}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    'threads_json': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'comments_json': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

MAINTENANCE_MODE = False

CORS_ORIGIN_ALLOW_ALL = True
