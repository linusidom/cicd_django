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
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']