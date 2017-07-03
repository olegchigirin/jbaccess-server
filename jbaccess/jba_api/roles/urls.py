from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', RolesController.as_view()),
    url(r'^(?P<id>\d+)$', RolesRUDController.as_view())
]
