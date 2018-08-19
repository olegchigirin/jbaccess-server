from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.place.PlacesViews import PlaceList, PlaceDetails, PlaceCreate, PlaceUpdate, \
    PlaceDelete, PlaceAttachedDoors, PlaceAttachDoors, PlaceDetachDoors

urlpatterns = [
    url(r'^$', login_required(PlaceList.as_view()), name='place list'),
    url(r'^(?P<id>\d+)/$', login_required(PlaceDetails.as_view()), name='place details'),
    url(r'^create/$', login_required(PlaceCreate.as_view()), name='place create'),
    url(r'^(?P<id>\d+)/update/$', login_required(PlaceUpdate.as_view()), name='place update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(PlaceDelete.as_view()), name='place delete'),
    url(r'^(?P<id>\d+)/doors/$', login_required(PlaceAttachedDoors.as_view()), name='place attached doors'),
    url(r'^(?P<id>\d+)/doors/attach/$', login_required(PlaceAttachDoors.as_view()), name='place attach doors'),
    url(r'^(?P<id>\d+)/doors/dettach/$', login_required(PlaceDetachDoors.as_view()), name='place detach doors'),
]
