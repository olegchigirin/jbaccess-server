from django.conf.urls import url

from .controllers import *

urlpatterns = [
    url(r'^$', SumController.as_view()),
]
