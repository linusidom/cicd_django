from todos.settings.base import *
import os

load_dotenv()

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

STATIC_DIR = 'static'
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static_root'

STATICFILES_DIRS = [STATIC_DIR]

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}