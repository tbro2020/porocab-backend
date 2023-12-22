"""
Django settings for poro project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!b7pgw_drg7zjvn05toj7qe(t#2l6a#fuo*lxm)%=oj)a^v%4k'
SECRET_KEY = os.getenv('SECRET_KEY', SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 1))
print('DEBUG:', DEBUG)

ALLOWED_HOSTS = []
ALLOWED_HOSTS = list(os.getenv('ALLOWED_HOSTS', '*').split(','))



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',

    'dal',
    'dal_select2',

    'tinymce',
    'mathfilters',
    'crispy_forms',
    'widget_tweaks',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_bootstrap5',
    'django_json_widget',

    'djmoney',
    'qr_code',
    'channels',
    'django_ace',
    'notifications',
    'phonenumber_field',

    'api',
    'core',
    'service'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'poro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context.base'
            ],
        },
    },
]

WSGI_APPLICATION = 'poro.wsgi.application'
ASGI_APPLICATION = 'poro.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if os.getenv('DATABASE_URL', None):
    DATABASES['default'] = dj_database_url.parse(os.getenv('DATABASE_URL'))

# Spatial settings
#SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'
#SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'
SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

print('DATABASES:', DATABASES.get('default', {}).get('ENGINE'))


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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-cd'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

print('LANGUAGE_CODE:', LANGUAGE_CODE)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_URL = os.getenv("STATIC_URL", STATIC_URL)
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = os.getenv("MEDIA_URL", 'media/')


AWS_LOCATION = os.getenv("AWS_LOCATION")
AWS_DEFAULT_ACL = os.getenv("AWS_DEFAULT_ACL")

AWS_S3_REGION = os.getenv("AWS_S3_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

STATICFILES_STORAGE = os.getenv("STATICFILES_STORAGE", 'django.contrib.staticfiles.storage.StaticFilesStorage')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth settings
LOGIN_URL = os.getenv("LOGIN_URL", 'login')
AUTH_USER_MODEL = os.getenv("AUTH_USER_MODEL", 'core.User')
LOGOUT_REDIRECT_URL = os.getenv("LOGOUT_REDIRECT_URL", 'login')
LOGIN_REDIRECT_URL = os.getenv("LOGIN_REDIRECT_URL", 'core:home')
    
# Email settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", EMAIL_BACKEND)
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", EMAIL_HOST_USER)
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", True)
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", False)

# Celery settings
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", 'redis://localhost:6379')


# Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# TinyMCE settings
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# Django Crispy Forms settings
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# Django Widget Tweaks settings
WIDGET_TWEAKS = {
    'error_class': 'is-invalid',
    'required_class': 'required',
    'form_group_class': 'mb-3',
}

# Django Ace settings
ACE_THEME = 'chrome'
ACE_MODES = [('python', 'Python')]

# Django Notifications settings
NOTIFICATIONS_SOFT_DELETE = True
NOTIFICATIONS_USE_JSONFIELD = True
NOTIFICATIONS_JSONFIELD_ENCODING = 'json'
NOTIFICATIONS_CONFIG = {
    'SOFT_DELETE': True,
    'USE_JSONFIELD': True,
    'JSONFIELD_ENCODING': 'json',
}

# Django Phonenumber Field settings
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_FORMAT = 'INTERNATIONAL'

PHONENUMBER_DEFAULT_REGION = 'CD'
PHONENUMBER_DEFAULT_FORMAT = 'E164'
PHONENUMBER_DEFAULT_FORMAT = 'RFC3966'

# Django channels settings
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('localhost', 6379)],
        },
    },
}

# DEBUG MODE
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    INSTALLED_APPS+=['debug_toolbar', 'django_extensions']
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')


# PRODUCTION MODE
if not DEBUG:
    INSTALLED_APPS.append('corsheaders')

    INDEX_OF_COMMON_MIDDLEWARE = MIDDLEWARE.index('django.middleware.common.CommonMiddleware')
    MIDDLEWARE.insert(INDEX_OF_COMMON_MIDDLEWARE, 'corsheaders.middleware.CorsMiddleware')

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'same-origin'

    # Security settings
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_HOST = True

    # CORS settings
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    CORS_ORIGIN_WHITELIST = os.getenv("CORS_ORIGIN_WHITELIST", '*').split(',')

    # Monitoring settings
    import json
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    SENTRY_DSN = os.getenv("SENTRY_DSN")
    SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT", 'production')
    SENTRY_RELEASE = os.getenv("SENTRY_RELEASE", '1.0.0')
    SENTRY_TRACES_SAMPLE_RATE = os.getenv("SENTRY_TRACES_SAMPLE_RATE", 0.5)
    SENTRY_TRACES_SAMPLE_RATE = float(SENTRY_TRACES_SAMPLE_RATE)
    SENTRY_TRACE_SAMPLING = os.getenv("SENTRY_TRACE_SAMPLING", 0.5)
    SENTRY_TRACE_SAMPLING = float(SENTRY_TRACE_SAMPLING)
    SENTRY_TRANSPORT = os.getenv("SENTRY_TRANSPORT", 'sentry_sdk.transport.HttpTransport')
    SENTRY_TRANSPORT_OPTIONS = os.getenv("SENTRY_TRANSPORT_OPTIONS", '{}')
    SENTRY_TRANSPORT_OPTIONS = json.loads(SENTRY_TRANSPORT_OPTIONS)

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=SENTRY_ENVIRONMENT,
        release=SENTRY_RELEASE,
        traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
        trace_sampling=SENTRY_TRACE_SAMPLING,
        transport=SENTRY_TRANSPORT,
        transport_options=SENTRY_TRANSPORT_OPTIONS,
        integrations=[DjangoIntegration()],
    )

    # Logging settings
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'WARNING',
                'class': 'sentry_sdk.integrations.logging.EventHandler',
                'formatter': 'verbose',
            },
            'console': {
                'level': 'WARNING',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.server': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.security': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.request': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.db.backends': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry_sdk': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry_sdk.errors': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry_sdk.integrations': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry_sdk.transport': {
                'level': 'WARNING',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

# Django money settings
DEFAULT_CURRENCY = 'CDF'

CURRENCY_CHOICES = [
    ('USD', 'USD'),
    ('CDF', 'CDF'),
]

# Ride settings
PRICE_PER_MINUTE = 350
PRICE_PER_MINUTE = int(os.getenv('PRICE_PER_MINUTE', PRICE_PER_MINUTE))
