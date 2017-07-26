from jba_server.settings.base import *
import os
import dj_database_url

SECRET_KEY = 'skj435h5lrkfsj;r34prosafdlkmc;alskfl905hok6jfIs'

DEBUG = False

DEFAULT_LOG_LEVEL = 'INFO'

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': DEFAULT_LOG_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # },
        'root': {
            'handlers': ['console', ],
            'level': DEFAULT_LOG_LEVEL,
        },
        'django.request': {
            'handlers': ['console', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', ],
            'propagate': True,
            'level': DEFAULT_LOG_LEVEL,
        },
    }
}

ALLOWED_HOSTS = ['*']
