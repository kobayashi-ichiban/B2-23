from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=qjyd)ymj!seoh*rbh+wsf_7sc0s+ws@lq%(dfpk^_723yz!36'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガー設定
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラー設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },

    # ハンドラー設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
