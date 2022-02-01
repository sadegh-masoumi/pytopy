from core.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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
    os.path.join(BASE_DIR, 'statics')
]
MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')
MEDIA_ROOT = "/home/pytopyir/public_html/media"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')
STATIC_ROOT = "/home/pytopyir/public_html/static"

