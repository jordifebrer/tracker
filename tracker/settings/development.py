from .common import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'testing_secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
