from django.conf.urls import url

from jba_ui.views.role.RoleViews import RoleList, RoleCreate, RoleDetail, RoleUpdate, RoleDelete, AttachPersonsToRole

urlpatterns = [
    # Roles urls
    url(r'^role/$', RoleList.as_view(), name='role list'),
    url(r'^role/create/$', RoleCreate.as_view(), name='role create'),
    url(r'^role/(?P<id>\d+)/$', RoleDetail.as_view(), name='role details'),
    url(r'^role/(?P<id>\d+)/update/$', RoleUpdate.as_view(), name='role update'),
    url(r'^role/(?P<id>\d+)/delete/$', RoleDelete.as_view(), name='role delete'),
    url(r'^role/(?P<id>\d+)/attach/$', AttachPersonsToRole.as_view(), name='role attach to person'),
]
