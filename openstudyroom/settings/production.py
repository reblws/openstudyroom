from __future__ import absolute_import, unicode_literals

# pylint: disable=import-error,wildcard-import,unused-wildcard-import

from .base import *


DEBUG = False

with open('/etc/db_pass.txt') as f:
    DB_PASS = f.read().strip()
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'openstudyroom',
        'USER': 'osr',
        'PASSWORD' : DB_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['openstudyroom.org', 'dev.openstudyroom.org']

DJANGO_CRON_DELETE_LOGS_OLDER_THAN = 7

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

with open('/etc/gmail_pass.txt') as f:
    GMAIL_PASS = f.read().strip()
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = GMAIL_PASS
EMAIL_HOST_USER = 'openstudyroom@gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


RAVEN_CONFIG = {
    'dsn': 'https://4fc2585f995348249682113f91124169:0e0c5bc2df38456090293fc24e43ce76@sentry.io/240861',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    #'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

with open('/etc/discord_secret.txt') as f:
    discord_secret = f.read().strip()
DISCORD_CLIENT_ID = "404373699287056385"
DISCORD_CLIENT_SECRET = discord_secret
