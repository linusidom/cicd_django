from todos.settings.base import *
import os

load_dotenv()

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dp5xg1mxd',
    'API_KEY': '232755111823242',
    'API_SECRET': 'PpyjasRhAWy-PHL26Xxpdpkz1gY',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'