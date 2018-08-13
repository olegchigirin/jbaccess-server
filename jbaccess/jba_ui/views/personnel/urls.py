from django.conf.urls import url

from jba_ui.views.personnel.PersonnelViews import PersonList, PersonCreate, PersonDetails, PersonUpdate, PersonDelete, \
    RolesAttachedToPerson, AttachRolesToPerson, DetachRolesFromPerson, AttachedKeysToPerson, AttachKeyToPerson, \
    PersonAllowedPlaces, PersonAllowPlaces, PersonDenyPlaces

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='person list'),
    url(r'^create/$', PersonCreate.as_view(), name='person create'),
    url(r'^(?P<id>\d+)/$', PersonDetails.as_view(), name='person details'),
    url(r'^(?P<id>\d+)/update/$', PersonUpdate.as_view(), name='person update'),
    url(r'^(?P<id>\d+)/delete/$', PersonDelete.as_view(), name='person delete'),
    url(r'^(?P<id>\d+)/roles/attached/$', RolesAttachedToPerson.as_view(), name='person attached roles'),
    url(r'^(?P<id>\d+)/roles/attach/$', AttachRolesToPerson.as_view(), name='person attach roles'),
    url(r'^(?P<id>\d+)/roles/detach/$', DetachRolesFromPerson.as_view(), name='person detach roles'),
    url(r'^(?P<id>\d+)/keys/attached/$', AttachedKeysToPerson.as_view(), name='person attached keys'),
    url(r'^(?P<id>\d+)/keys/create/$', AttachKeyToPerson.as_view(), name='person attach key'),
    url(r'^(?P<id>\d+)/allowed/$', PersonAllowedPlaces.as_view(), name='person acl rules'),
    url(r'^(?P<id>\d+)/allow/$', PersonAllowPlaces.as_view(), name='person acl allow'),
    url(r'^(?P<id>\d+)/deny/$', PersonDenyPlaces.as_view(), name='person acl deny'),
]
