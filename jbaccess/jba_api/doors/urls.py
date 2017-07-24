from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', DoorsController.as_view()),
    url(r'^(?P<id>\d+)$', DoorsRUDController.as_view()),
]
