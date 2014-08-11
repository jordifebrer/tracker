from .common import *


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    os.environ['TRACKER_ALLOWED_HOST'],
]

SECRET_KEY = os.environ['TRACKER_SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['TRACKER_DB_NAME'],
        'USER': os.environ['TRACKER_DB_USER'],
        'PASS': os.environ.get('TRACKER_DB_PASS'),
        'HOST': os.environ.get('TRACKER_DB_HOST', ''),
        'PORT': os.environ.get('TRACKER_DB_PORT', '5432'),
    },
}
