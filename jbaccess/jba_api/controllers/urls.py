from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', ControllersController.as_view()),
    url(r'^(?P<id>\d+)$', ControllersRUDController.as_view()),
]