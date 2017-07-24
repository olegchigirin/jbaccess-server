from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^login$', LoginController.as_view()),
    url(r'^logout$', LogoutController.as_view()),
    url(r'^restore-session$', RestoreSessionController.as_view())
]