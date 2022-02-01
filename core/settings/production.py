from core.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
is_test_net = os.environ.get('is_test_net')
if is_test_net == 'False':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pytopyir_PyDatabase',
            'USER': 'pytopyir_PyToPy_main',
            'PASSWORD': '^6zC9359005490.ms',
            'HOST': 'localhost',
            'POST': '3306',
            'OPTIONS': {
                'sql_mode': 'STRICT_ALL_TABLES'
            }
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
        '*'
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pytopyir_test_net',
            'USER': 'pytopyir_test_net_user',
            'PASSWORD': 'r2+1}aWu~Bk]',
            'HOST': 'localhost',
            'POST': '3306',
            'OPTIONS': {
                'sql_mode': 'STRICT_ALL_TABLES'
            }
        }
    }
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]
MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')
MEDIA_ROOT = "/home/pytopyir/public_html/media"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')
STATIC_ROOT = "/home/pytopyir/public_html/static"

# CORS configs
CORS_ALLOWED_ORIGINS = [

    'http://pytopy.ir',
    'https://pytopy.ir',
    'http://www.pytopy.ir',
    'https://www.pytopy.ir',

    'http://127.0.0.1:8000',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.pytopy\.ir",
    'http://127.0.0.1:8000',

]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# REST_FRAMEWORK

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
