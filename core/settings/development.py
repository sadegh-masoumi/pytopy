from core.settings.base import *

ALLOWED_HOSTS = ['*']

# Database conf

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

# static file
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'cdn', 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'cdn', 'media_root')
