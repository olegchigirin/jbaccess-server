from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', RolesController.as_view()),
    url(r'^(?P<id>\d+)$', RolesRUDController.as_view()),
    url(r'^(?P<id>\d+)/acls$', RolePlaceGetAclsController.as_view()),
    url(r'^(?P<role_id>\d+)/allow/(?P<place_id>\d+)$', RoleAllowPlaceController.as_view()),
    url(r'^(?P<role_id>\d+)/deny/(?P<place_id>\d+)$', RoleDenyPlaceController.as_view())
]
