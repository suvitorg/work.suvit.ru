import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{remote_dir}}/data/base.sqlite',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 300,
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = 'suvitatwork'

MEDIA_ROOT = os.path.join('{{remote_dir}}', 'media', 'media')
STATIC_ROOT = os.path.join('{{remote_dir}}', 'media', 'static')
