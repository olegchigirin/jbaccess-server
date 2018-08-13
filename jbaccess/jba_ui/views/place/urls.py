from django.conf.urls import url

from jba_ui.views.place.PlacesViews import PlaceList, PlaceDetails, PlaceCreate, PlaceUpdate, \
    PlaceDelete, PlaceAttachedDoors, PlaceAttachDoors, PlaceDetachDoors

urlpatterns = [
    url(r'^$', PlaceList.as_view(), name='place list'),
    url(r'^(?P<id>\d+)/$', PlaceDetails.as_view(), name='place details'),
    url(r'^create/$', PlaceCreate.as_view(), name='place create'),
    url(r'^(?P<id>\d+)/update/$', PlaceUpdate.as_view(), name='place update'),
    url(r'^(?P<id>\d+)/delete/$', PlaceDelete.as_view(), name='place delete'),
    url(r'^(?P<id>\d+)/doors/$', PlaceAttachedDoors.as_view(), name='place attached doors'),
    url(r'^(?P<id>\d+)/doors/attach/$', PlaceAttachDoors.as_view(), name='place attach doors'),
    url(r'^(?P<id>\d+)/doors/dettach/$', PlaceDetachDoors.as_view(), name='place detach doors'),
]
