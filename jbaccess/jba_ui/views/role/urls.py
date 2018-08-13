from django.conf.urls import url

from jba_ui.views.role.RoleViews import RoleList, RoleCreate, RoleDetail, RoleUpdate, RoleDelete, AttachPersonsToRole, \
    AttachedPersonsToRole, DetachPersonsFromRole, RoleAllowedPlaces, RoleAllowPlaces, RoleDenyPlaces

urlpatterns = [
    # Roles urls
    url(r'^$', RoleList.as_view(), name='role list'),
    url(r'^create/$', RoleCreate.as_view(), name='role create'),
    url(r'^(?P<id>\d+)/$', RoleDetail.as_view(), name='role details'),
    url(r'^(?P<id>\d+)/update/$', RoleUpdate.as_view(), name='role update'),
    url(r'^(?P<id>\d+)/delete/$', RoleDelete.as_view(), name='role delete'),
    url(r'^(?P<id>\d+)/persons/attached/$', AttachedPersonsToRole.as_view(), name='role attached persons'),
    url(r'^(?P<id>\d+)/persons/attach/$', AttachPersonsToRole.as_view(), name='role attach persons'),
    url(r'^(?P<id>\d+)/persons/detach/$', DetachPersonsFromRole.as_view(), name='role detach persons'),
    url(r'^(?P<id>\d+)/allowed/$', RoleAllowedPlaces.as_view(), name='role acl rules'),
    url(r'^(?P<id>\d+)/allow/$', RoleAllowPlaces.as_view(), name='role acl allow'),
    url(r'^(?P<id>\d+)/deny/$', RoleDenyPlaces.as_view(), name='role acl deny')
]
