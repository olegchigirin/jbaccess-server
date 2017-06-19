from django.conf.urls import url

from .controllers import *

urlpatterns = [
    url(r'^ping$', PingController.as_view()),
]
