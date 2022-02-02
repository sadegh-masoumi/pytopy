# SECURITY WARNING: don't run with debug turned on in production!
from core.settings.base import *

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# debug toolbar

INTERNAL_IPS = [
    '127.0.0.1',
]

# MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
# INSTALLED_APPS.append('debug_toolbar')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'cdn', 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'cdn', 'media_root')

