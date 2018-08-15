from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.personnel.PersonnelViews import PersonList, PersonCreate, PersonDetails, PersonUpdate, PersonDelete, \
    RolesAttachedToPerson, AttachRolesToPerson, DetachRolesFromPerson, AttachedKeysToPerson, AttachKeyToPerson, \
    PersonAllowedPlaces, PersonAllowPlaces, PersonDenyPlaces

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='person list'),
    url(r'^create/$', login_required(PersonCreate.as_view()), name='person create'),
    url(r'^(?P<id>\d+)/$', PersonDetails.as_view(), name='person details'),
    url(r'^(?P<id>\d+)/update/$', login_required(PersonUpdate.as_view()), name='person update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(PersonDelete.as_view()), name='person delete'),
    url(r'^(?P<id>\d+)/roles/attached/$', RolesAttachedToPerson.as_view(), name='person attached roles'),
    url(r'^(?P<id>\d+)/roles/attach/$', login_required(AttachRolesToPerson.as_view()), name='person attach roles'),
    url(r'^(?P<id>\d+)/roles/detach/$', login_required(DetachRolesFromPerson.as_view()), name='person detach roles'),
    url(r'^(?P<id>\d+)/keys/attached/$', AttachedKeysToPerson.as_view(), name='person attached keys'),
    url(r'^(?P<id>\d+)/keys/create/$', login_required(AttachKeyToPerson.as_view()), name='person attach key'),
    url(r'^(?P<id>\d+)/allowed/$', PersonAllowedPlaces.as_view(), name='person acl rules'),
    url(r'^(?P<id>\d+)/allow/$', login_required(PersonAllowPlaces.as_view()), name='person acl allow'),
    url(r'^(?P<id>\d+)/deny/$', login_required(PersonDenyPlaces.as_view()), name='person acl deny'),
]
