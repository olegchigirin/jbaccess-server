from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', ControllersController.as_view()),
    url(r'^(?P<id>\d+)$', ControllersRUDController.as_view()),
    url(r'^(?P<id>\d+)/doors$', GetDoorsController.as_view()),
    url(r'^(?P<controller_id>\d+)/doors/(?P<door_id>\d+)$', ControllerDoorRelationController.as_view()),
]