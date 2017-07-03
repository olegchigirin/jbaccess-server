from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', KeysController.as_view()),
    url(r'^(?P<id>\d+)$', KeysRUDController.as_view())
]
