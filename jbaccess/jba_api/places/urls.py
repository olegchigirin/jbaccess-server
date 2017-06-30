from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', PlacesController.as_view()),
    url(r'^(?P<id>\d+)$', PlacesRUDController.as_view()),
    url(r'^(?P<id>\d+)/doors$', GetDoorsController.as_view()),
    url(r'^(?P<place_id>\d+)/doors/(?P<door_id>\d+)$', PlacesDoorRelationController.as_view())
]
