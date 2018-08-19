from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.personnel.PersonnelViews import PersonList, PersonCreate, PersonDetails, PersonUpdate, PersonDelete, \
    RolesAttachedToPerson, AttachRolesToPerson, DetachRolesFromPerson, AttachedKeysToPerson, CreateKeyForPerson, \
    PersonAclsRules, PersonAllowPlaces, PersonDenyPlaces

urlpatterns = [
    url(r'^$', login_required(PersonList.as_view()), name='person list'),
    url(r'^create/$', login_required(PersonCreate.as_view()), name='person create'),
    url(r'^(?P<id>\d+)/$', login_required(PersonDetails.as_view()), name='person details'),
    url(r'^(?P<id>\d+)/update/$', login_required(PersonUpdate.as_view()), name='person update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(PersonDelete.as_view()), name='person delete'),
    url(r'^(?P<id>\d+)/roles/attached/$', RolesAttachedToPerson.as_view(), name='person attached roles'),
    url(r'^(?P<id>\d+)/roles/attach/$', login_required(AttachRolesToPerson.as_view()), name='person attach roles'),
    url(r'^(?P<id>\d+)/roles/detach/$', login_required(DetachRolesFromPerson.as_view()), name='person detach roles'),
    url(r'^(?P<id>\d+)/keys/attached/$', login_required(AttachedKeysToPerson.as_view()), name='person attached keys'),
    url(r'^(?P<id>\d+)/keys/create/$', login_required(CreateKeyForPerson.as_view()), name='person attach key'),
    url(r'^(?P<id>\d+)/allowed/$', login_required(PersonAclsRules.as_view()), name='person acl rules'),
    url(r'^(?P<id>\d+)/allow/$', login_required(PersonAllowPlaces.as_view()), name='person acl allow'),
    url(r'^(?P<id>\d+)/deny/$', login_required(PersonDenyPlaces.as_view()), name='person acl deny'),
]
