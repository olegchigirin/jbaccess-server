from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.controller.ControllerViews import ControllerList, ControllerDetails, ControllerCreate, \
    ControllerUpdate, ControllerDelete, ControllerAttachedDoors, ControllerAttachDoors, ControllerDetachDoors, \
    ControllerResolveAcls

urlpatterns = [
    url(r'^$', login_required(ControllerList.as_view()), name='controller list'),
    url(r'^create/$', login_required(ControllerCreate.as_view()), name='controller create'),
    url(r'^(?P<id>\w+)/$', login_required(ControllerDetails.as_view()), name='controller details'),
    url(r'^(?P<id>\w+)/update/$', login_required(ControllerUpdate.as_view()), name='controller update'),
    url(r'^(?P<id>\w+)/delete/$', login_required(ControllerDelete.as_view()), name='controller delete'),
    url(r'^(?P<id>\w+)/doors/$', login_required(ControllerAttachedDoors.as_view()), name='controller attached doors'),
    url(r'^(?P<id>\w+)/doors/attach/$', login_required(ControllerAttachDoors.as_view()), name='controller attach doors'),
    url(r'^(?P<id>\w+)/doors/detach/$', login_required(ControllerDetachDoors.as_view()), name='controller detach doors'),
    url(r'^(?P<id>\w+)/resolve', login_required(ControllerResolveAcls.as_view()), name='controller resolve acls')

]
