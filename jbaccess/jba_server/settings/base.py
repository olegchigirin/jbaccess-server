import socket
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERSION = "1.0.0"
API_VERSION = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'skj435h5lrkfsj;r34prosafdlkmc;alskfl905hok6jfIs'
DEBUG = False
ALLOWED_HOSTS = []

STATIC_ROOT = './staticfiles/'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

from .app_structure import *
from version_meta import *