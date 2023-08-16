"""
Django settings for mbsocialweb project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import environ
import redis

from pathlib import Path
from firebase_admin import credentials, initialize_app

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

GOOGLE_RECAPTCHA_SITE_KEY = env('GOOGLE_RECAPTCHA_SITE_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = env('GOOGLE_RECAPTCHA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = env('DEBUG')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # SITEMAP
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	# MIS APPS
    'about.apps.AboutConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'core.apps.CoreConfig',
    'ckeditor',
    'ckeditor_uploader',
    'debug_toolbar',
    'graphicdesign.apps.GraphicdesignConfig',
    'marketing.apps.MarketingConfig',
    'social.apps.SocialConfig',
    'page.apps.PageConfig',
    'portfolio.apps.PortfolioConfig',
    'socialmedia.apps.SocialmediaConfig',
    'taggit',
    'webdesign.apps.WebdesignConfig',
    'pwa',
    'fcm_django',
]

SITE_ID = 1

CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mbsocialweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.processors.ctx_dict',
                'mbsocialweb.processors.canonical',
            ],
        },
    },
]

WSGI_APPLICATION = 'mbsocialweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# Redis Cache
# https://docs.djangoproject.com/en/4.2/topics/cache/#redis

# django-redis
# https://github.com/jazzband/django-redis

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://default:' + env('REDIS_PASSWORD') + '@' + env('REDIS_HOST') + ':' + env('REDIS_PORT'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'static'

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
            'full',
        'extraPlugins':
            ','.join([
                'image2',  # the upload image feature
                # your extra plugins here
                'div'
            ]),
    }
}

# Pwa
# PWA_SERVICE_WORKER_PATH = BASE_DIR / 'core/static/core/js' / 'pwaworker.js'
# Para produccion
# PWA_SERVICE_WORKER_PATH = BASE_DIR / 'static/core/js' / 'pwaworker.js'
# Para desarrollo
PWA_SERVICE_WORKER_PATH = BASE_DIR / 'core/static/core/js' / 'pwaworker.js'
PWA_APP_NAME = 'mbSocialWeb'
PWA_APP_DESCRIPTION = "mbSocialWeb PWA"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/core/img/favi.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/core/img/favi.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/core/img/favi.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-ES'

# FCM_DJANGO
# GOOGLE_APPLICATION_CREDENTIALS = os.path.join(BASE_DIR, './credentials.json')
GOOGLE_APPLICATION_CREDENTIALS = BASE_DIR / './credentials.json'

cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
initialize_app(cred)

FCM_DJANGO_SETTINGS = {
    # an instance of firebase_admin.App to be used as default for all fcm-django requests
    # default: None (the default Firebase app)
    # "DEFAULT_FIREBASE_APP": None,
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "noti-mbSocialWeb",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": True,
    # Transform create of an existing Device (based on registration id) into
    # True solo funciona con django rest framework
    # an update. See the section
    # "Update of device with duplicate registration ID" for more details.
    # default: False
    "UPDATE_ON_DUPLICATE_REG_ID": False,
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
