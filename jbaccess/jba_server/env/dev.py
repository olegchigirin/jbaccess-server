from jba_server.settings.base import *
import os

DEBUG = True

DEFAULT_LOG_LEVEL = 'DEBUG'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jbaccess.sqlite3'
    }
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
            'level': 'DEBUG',
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