from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', PersonController.as_view()),
    url(r'^(?P<id>\d+)$', PersonRUDController.as_view()),
    url(r'^(?P<id>\d+)/keys$', GetKeysController.as_view()),
    url(r'^(?P<id>\d+)/roles$', GetRolesController.as_view()),
    url(r'^(?P<person_id>\d+)/roles/(?P<role_id>\d+)$', PersonRolesCDController.as_view()),
    url(r'^(?P<person_id>\d+)/allow/(?P<place_id>\d+)$', PersonAllowPlaceController.as_view()),
    url(r'^(?P<person_id>\d+)/deny/(?P<place_id>\d+)$', PersonDenyPlaceController.as_view()),
    url(r'^(?P<id>\d+)/acls$', PersonPlaceGetAclsController.as_view())
]
