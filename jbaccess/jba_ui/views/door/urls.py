from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.door.DoorViews import DoorList, DoorDetails, DoorCreate, DoorUpdate, DoorDelete, \
    DoorAttachedControllers, DoorAttachControllers, DoorDetachControllers, DoorAttachedPlaces, DoorAttachPlaces, \
    DoorDetachPlaces

urlpatterns = [

    url(r'^$', login_required(DoorList.as_view()), name='door list'),
    url(r'^(?P<id>\d+)/$', login_required(DoorDetails.as_view()), name='door details'),
    url(r'^create', login_required(DoorCreate.as_view()), name='door create'),
    url(r'^(?P<id>\d+)/update/$', login_required(DoorUpdate.as_view()), name='door update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(DoorDelete.as_view()), name='door delete'),
    url(r'^(?P<id>\d+)/controllers/$', login_required(DoorAttachedControllers.as_view()), name='door attached controllers'),
    url(r'^(?P<id>\d+)/controllers/attach/$', login_required(DoorAttachControllers.as_view()),
        name='door attach controllers'),
    url(r'^(?P<id>\d+)/controllers/detach/$', login_required(DoorDetachControllers.as_view()),
        name='door detach controllers'),
    url(r'^(?P<id>\d+)/places/$', login_required(DoorAttachedPlaces.as_view()), name='door attached places'),
    url(r'^(?P<id>\d+)/places/attach/$', login_required(DoorAttachPlaces.as_view()), name='door attach places'),
    url(r'^(?P<id>\d+)/places/detach/$', login_required(DoorDetachPlaces.as_view()), name='door detach places'),

]
