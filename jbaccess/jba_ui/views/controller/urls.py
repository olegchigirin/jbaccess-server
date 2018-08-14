from django.conf.urls import url

from jba_ui.views.controller.ControllerViews import ControllerList, ControllerDetails, ControllerCreate, \
    ControllerUpdate, ControllerDelete, ControllerAttachedDoors, ControllerAttachDoors, ControllerDetachDoors, \
    ControllerResolveAcls

urlpatterns = [
    url(r'^$', ControllerList.as_view(), name='controller list'),
    url(r'^create/$', ControllerCreate.as_view(), name='controller create'),
    url(r'^(?P<id>\w+)/$', ControllerDetails.as_view(), name='controller details'),
    url(r'^(?P<id>\w+)/update/$', ControllerUpdate.as_view(), name='controller update'),
    url(r'^(?P<id>\w+)/delete/$', ControllerDelete.as_view(), name='controller delete'),
    url(r'^(?P<id>\w+)/doors/$', ControllerAttachedDoors.as_view(), name='controller attached doors'),
    url(r'^(?P<id>\w+)/doors/attach/$', ControllerAttachDoors.as_view(), name='controller attach doors'),
    url(r'^(?P<id>\w+)/doors/detach/$', ControllerDetachDoors.as_view(), name='controller detach doors'),
    url(r'^(?P<id>\w+)/resolve', ControllerResolveAcls.as_view(), name='controller resolve acls')

]
