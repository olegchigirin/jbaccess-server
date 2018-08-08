from django.conf.urls import url

from jba_ui.views.personnel.PersonnelViews import PersonList, PersonCreate, PersonDetail, PersonUpdate, PersonDelete, \
    RolesAttachedToPerson, AttachRolesToPerson, DetachRolesFromPerson, AttachedKeysToPerson, AttachKeysToPerson, \
    DetachKeysFromPerson

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='person list'),
    url(r'^create/$', PersonCreate.as_view(), name='person create'),
    url(r'^(?P<id>\d+)/$', PersonDetail.as_view(), name='person details'),
    url(r'^(?P<id>\d+)/update/$', PersonUpdate.as_view(), name='person update'),
    url(r'^(?P<id>\d+)/delete/$', PersonDelete.as_view(), name='person delete'),
    url(r'^(?P<id>\d+)/roles/attached/$', RolesAttachedToPerson.as_view(), name='person attached roles'),
    url(r'^(?P<id>\d+)/roles/attach/$', AttachRolesToPerson.as_view(), name='person attach roles'),
    url(r'^(?P<id>\d+)/roles/detach/$', DetachRolesFromPerson.as_view(), name='person detach roles'),
    url(r'^(?P<id>\d+)/keys/attached/$', AttachedKeysToPerson.as_view(), name='person attached keys'),
    url(r'^(?P<id>\d+)/keys/attach/$', AttachKeysToPerson.as_view(), name='person attach key'),
    url(r'^(?P<id>\d+)/keys/detach/$', DetachKeysFromPerson.as_view(), name='person detach key'),
]
