# Standart Library.
import os
from decouple import config
from dj_database_url import parse as dburl

# Local Django.
from theory import constants as theory_constants

"""
Django settings for CodaMais project.
Generated by 'django-admin startproject' using Django 1.10.6.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

# Information needed to send the email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'codamaisapp@gmail.com'
EMAIL_HOST_PASSWORD = 'codamais'
EMAIL_PORT = 587


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']


# Application definition.

INSTALLED_APPS = [
    'user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'theory',
    'exercise',
    'redactor',
    'landing',
    'forum',
    'dashboard',
    'ranking',
    'achievement',
]

# Authentication backends
AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'CodaMais.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': ['templates', 'user/templates', 'exercise/templates_exercise',
                 'landing/templates', 'dashboard/templates', 'forum/templates_forum',
                 'ranking/templates', 'theory/templates'],

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

WSGI_APPLICATION = 'CodaMais.wsgi.application'


# Database.
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

# User model

AUTH_USER_MODEL = "user.User"

# Password validation.
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization.
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LOCALE_PATHS = [
          '/home/rdlenke/workspace/CodaMais/CodaMais/user/locale',
]

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', u'English'),
    ('pt-br', u'Portugues'),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, Java, Images).
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Configurations for the django-wysiwyg-redactor: Redactor WYSIWYG editor.
# https://imperavi.com/redactor/.

REDACTOR_OPTIONS = {'lang': 'en',
                    'focus': True,
                    'placeholder': theory_constants.REDACTOR_PLACEHOLDER,
                    'minHeight': theory_constants.MIN_REDACTOR_HEIGHT,
                    'buttonsHide': ['file', 'video'],
                    'imageResizable': True,
                    'imagePosition': True,
                    'plugins': ['inlinestyle',
                                'table',
                                'source',
                                'fontcolor',
                                'fontfamily',
                                'fontsize',
                                'fullscreen']
                    }

# Logging system

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'default': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

REDACTOR_UPLOAD = 'redactor_uploads/'
REDACTOR_UPLOAD_HANDLER = 'redactor.handlers.SimpleUploader'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

LOGIN_URL = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
