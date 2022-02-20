import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-)&-1w3as5lbnu00-#z^pkt*szl*9tmh#6p-iq(byqzb6ee%84q'

DEBUG = os.environ.get('DEBUG', default='debug') == 'debug'
is_test_net = os.environ.get('DEBUG') == 'testnet'

# download file api
DOWNLOAD_API = 'http://127.0.0.1:5000/' if DEBUG else 'https://download.pytopy.ir/'
# token for download. subdomain
PYTOPY_TOKEN = 'c45dhk@|!(&^NLDjn687vhk.seg66:'
# zarin pal
MERCHANT_ID = '6d1c6f92-57e9-4d33-b922-6fda2424b34f'

UPDATE_TOKEN = 'knk32r3d^&*IU&(G'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #  our apps
    'django_render_partial',

    'app_home.apps.AppHomeConfig',
    'app_user.apps.AppUserConfig',
    'app_course.apps.AppCourseConfig',
    'app_category.apps.AppCategoryConfig',
    'app_contact_us.apps.AppContactUsConfig',
    'app_article.apps.AppArticleConfig',
    'app_about_us.apps.AppAboutUsConfig',
    'app_work_with_us.apps.AppWorkWithUsConfig',
    'app_dashboard.apps.AppDashboardConfig',
    'app_order.apps.AppOrderConfig',
    'app_404.apps.App404Config'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
AUTH_USER_MODEL = 'app_user.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # ----------- render partial ---------------
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
