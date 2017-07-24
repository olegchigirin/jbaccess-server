import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'jba_server.env.' + os.environ.get('ENV', 'dev'))
application = get_wsgi_application()
