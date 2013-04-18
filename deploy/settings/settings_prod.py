import os
import json
from unipath import FSPath as Path

# The full path to the django_website directory.
BASE = Path(__file__).absolute().ancestor(2)
SECRETS = json.load(open(BASE.ancestor(1).child('secrets.json')))

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

SENTRY_DSN = str(SECRETS['sentry_dsn'])

{{settings_logging}}
