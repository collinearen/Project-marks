from pathlib import Path

from django.urls import reverse_lazy

from pythonjsonlogger.jsonlogger import JsonFormatter

from account.logging_formatters import CustomJsonFormatter

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-c1bkqgegjaz=lh@wlc29xei-isl$=8nkow6^a09#m7@t%w*-tz'
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'easy_thumbnails',
    'images.apps.ImagesConfig',
    'actions.apps.ActionsConfig',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'share.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'share.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shareit',
        'USER': 'postgres',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_format': {
            'format': "{asctime}    {levelname}    {filename}    {message}",
            'style': "{"
        },
        'json_formatter': {
            '()': CustomJsonFormatter,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # На консоль я оставлю main formatter, так как было изначально в Django
            'formatter': 'main_format',
        },

        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_formatter',
            # А на запись в файл я поставлю json formatter
            'filename': "information.log"
        }
    },
    'loggers': {
        "main": {
            "handlers": ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'AIzaSyCe-mUlP4c_CVtvCAIVZrag0PCpmbCNUf0'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
]

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail',
                                        args=[u.username])
}

INTERNAL_IPS = [
    '127.0.0.1',
]

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

if DEBUG:
    import mimetypes

mimetypes.add_type('application/javascript', '.js', True)
mimetypes.add_type('text/css', '.css', True)

# <-- EMAIL YANDEX-->

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "ihecore2@yandex.ru"
EMAIL_HOST_PASSWORD = 'bdrhimzttcfbgwks'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

# <--- RUNSERVER --->
# python manage.py runserver_plus --cert-file cert.crt