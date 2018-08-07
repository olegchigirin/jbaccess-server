from django.conf.urls import url

from jba_ui.views.door.DoorViews import DoorList, DoorDetails, DoorCreate, DoorUpdate, DoorDelete

urlpatterns = [

    url(r'^$', DoorList.as_view(), name='door list'),
    url(r'^(?P<id>\d+)/$', DoorDetails.as_view(), name='door details'),
    url(r'^create', DoorCreate.as_view(), name='door create'),
    url(r'^(?P<id>\d+)/update$', DoorUpdate.as_view(), name='door update'),
    url(r'^(?P<id>\d+)/delete$', DoorDelete.as_view(), name='door delete'),

]
