# -*- coding: utf-8 -*-
# Django settings for suvitatwork project.

import os
import json
from unipath import FSPath as Path

# The full path to the django_website directory.
BASE = Path(__file__).absolute().ancestor(2)
SECRETS = json.load(open(BASE.ancestor(1).child('secrets.json')))

# Far too clever trick to know if we're running on the deployment server.
PRODUCTION = ('DJANGOPROJECT_DEBUG' not in os.environ)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'base.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Yekaterinburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = BASE + '/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = str(SECRETS['secret_key'])

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
]
if PRODUCTION:
    MIDDLEWARE_CLASSES.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
    MIDDLEWARE_CLASSES.append('django.middleware.cache.FetchFromCacheMiddleware')


ROOT_URLCONF = 'suvitatwork.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'suvitatwork.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(Path(__file__).ancestor(1), 'theme', "templates"),

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',

    'knowledge',

    'djangorestframework',
    'mptt',
    'compressor',
    'fiber',

    'userena',
    'userena.contrib.umessages',
    'guardian',
    'easy_thumbnails',
    'south',
    'sendsmsru',

    'suvitatwork.theme',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Log errors to Sentry instead of email, if available.
if 'sentry_dsn' in SECRETS:
    INSTALLED_APPS.append('raven.contrib.django')
    SENTRY_DSN = SECRETS['sentry_dsn']
    LOGGING["loggers"]["django.request"]["handlers"].remove("mail_admins")

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_PROFILE_MODULE = 'theme.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

ANONYMOUS_USER_ID = -1

from django.utils.datastructures import SortedDict

PLAN_FEATURES = SortedDict([
    ('contact', 'Прием заявок через'),
    ('work_time', 'Время приема заявок'),
    ('response_time', 'Время ответа на заявку'),
    ('include_hours', 'Количество часов включенных в план'),
    ('extra_hour_cost', 'Стоимость часа сверх включенных, руб'),
])

PLANS = [
    {'name': 'Бесплатный',
     'contact': ['email', 'smartnut'],
     'response_time': '2 недели',
     'note': 'Тариф действует только для сайтов из нашего портфолио',
     'include_hours': 0,
     'extra_hour_cost': 1200,
     'cost': 0,
    },
    {'name': 'Базовый',
     'contact': ['email', 'smartnut', 'phone'],
     'work_time': '5х8. с 10 до 19. перерыв с 13 до 14',
     'response_time': '8 часов',
     'include_hours': 5,
     'extra_hour_cost': 900,
     'cost': 5000,
    },
    {'name': 'Расширенный',
     'contact': ['email', 'smartnut', 'phone'],
     'work_time': '5х10. с 9 до 19',
     'response_time': '8 часов',
     'include_hours': 10,
     'extra_hour_cost': 600,
     'cost': 10000,
    },
    {'name': 'Круглосуточный',
     'contact': ['email', 'smartnut', 'phone'],
     'response_time': '4 часа',
     'work_time': '7х24. круглосуточно',
     'include_hours': 15,
     'extra_hour_cost': 450,
     'cost': 15000,
    },
]

SENDSMS_BACKEND = 'sendsmsru.backends.websmsru.HTTPClient'
SENDSMS_DEFAULT_FROM_PHONE = 'SUVIT'
WEBSMSRU_USERNAME = 'suvit'
WEBSMSRU_PASSWORD = 'Dy4t9a6Ahx'

try:
    from settings_local import *
except ImportError:
    pass
