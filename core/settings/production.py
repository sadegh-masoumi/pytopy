from core.settings.base import *

if not is_test_net:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pytopyir_PyDatabase',
            'USER': 'pytopyir_PyToPy_main',
            'PASSWORD': '^6zC9359005490.ms',
            'HOST': 'localhost',
            'POST': '5432',
        }
    }
    ALLOWED_HOSTS = [
        'pytopy.ir',
        'http://pytopy.ir/',
        'https://pytopy.ir/',
        'http://www.pytopy.ir/',
        'https://www.pytopy.ir/',
    ]

else:
    ALLOWED_HOSTS = [
        't-net.pytopy.ir',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]
MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')
MEDIA_ROOT = "/home/pytopyir/public_html/media"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')
STATIC_ROOT = "/home/pytopyir/public_html/static"
