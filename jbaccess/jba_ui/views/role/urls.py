from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.role.RoleViews import RoleList, RoleCreate, RoleDetail, RoleUpdate, RoleDelete, AttachPersonsToRole, \
    AttachedPersonsToRole, DetachPersonsFromRole, RoleAllowedPlaces, RoleAllowPlaces, RoleDenyPlaces

urlpatterns = [
    # Roles urls
    url(r'^$', RoleList.as_view(), name='role list'),
    url(r'^create/$', login_required(RoleCreate.as_view()), name='role create'),
    url(r'^(?P<id>\d+)/$', RoleDetail.as_view(), name='role details'),
    url(r'^(?P<id>\d+)/update/$', login_required(RoleUpdate.as_view()), name='role update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(RoleDelete.as_view()), name='role delete'),
    url(r'^(?P<id>\d+)/persons/attached/$', AttachedPersonsToRole.as_view(), name='role attached persons'),
    url(r'^(?P<id>\d+)/persons/attach/$', login_required(AttachPersonsToRole.as_view()), name='role attach persons'),
    url(r'^(?P<id>\d+)/persons/detach/$', login_required(DetachPersonsFromRole.as_view()), name='role detach persons'),
    url(r'^(?P<id>\d+)/allowed/$', RoleAllowedPlaces.as_view(), name='role acl rules'),
    url(r'^(?P<id>\d+)/allow/$', login_required(RoleAllowPlaces.as_view()), name='role acl allow'),
    url(r'^(?P<id>\d+)/deny/$', login_required(RoleDenyPlaces.as_view()), name='role acl deny'),
]
