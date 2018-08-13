from django.conf.urls import url

from jba_ui.views.door.DoorViews import DoorList, DoorDetails, DoorCreate, DoorUpdate, DoorDelete, \
    DoorAttachedControllers, DoorAttachControllers, DoorDetachControllers, DoorAttachedPlaces, DoorAttachPlaces, \
    DoorDetachPlaces

urlpatterns = [

    url(r'^$', DoorList.as_view(), name='door list'),
    url(r'^(?P<id>\d+)/$', DoorDetails.as_view(), name='door details'),
    url(r'^create', DoorCreate.as_view(), name='door create'),
    url(r'^(?P<id>\d+)/update/$', DoorUpdate.as_view(), name='door update'),
    url(r'^(?P<id>\d+)/delete/$', DoorDelete.as_view(), name='door delete'),
    url(r'^(?P<id>\d+)/controllers/$', DoorAttachedControllers.as_view(), name='door attached controllers'),
    url(r'^(?P<id>\d+)/controllers/attach/$', DoorAttachControllers.as_view(), name='door attach controllers'),
    url(r'^(?P<id>\d+)/controllers/detach/$', DoorDetachControllers.as_view(), name='door detach controllers'),
    url(r'^(?P<id>\d+)/places/$', DoorAttachedPlaces.as_view(), name='door attached places'),
    url(r'^(?P<id>\d+)/places/attach/$', DoorAttachPlaces.as_view(), name='door attach places'),
    url(r'^(?P<id>\d+)/places/detach/$', DoorDetachPlaces.as_view(), name='door detach places'),

]
