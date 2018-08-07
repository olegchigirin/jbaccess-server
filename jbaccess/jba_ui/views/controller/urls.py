from django.conf.urls import url

from jba_ui.views.controller.ControllerViews import ControllerList, ControllerDetails, ControllerCreate, \
    ControllerUpdate, ControllerDelete

urlpatterns = [
    url(r'^$', ControllerList.as_view(), name='controller list'),
    url(r'^(?P<id>\d+)/$', ControllerDetails.as_view(), name='controller details'),
    url(r'^create/$', ControllerCreate.as_view(), name='controller create'),
    url(r'^(?P<id>\d+)/update/$', ControllerUpdate.as_view(), name='controller update'),
    url(r'^(?P<id>\d+)/delete/$', ControllerDelete.as_view(), name='controller delete'),
]
