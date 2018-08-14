from django.conf.urls import url

from .ACLsViews import AclPatternDetails, AclPatternCreate, AclPatterns, AclPatternUpdate, AclPatternDelete, AclDelete

urlpatterns = [
    url(r'^(?P<id>\d+)/$', AclPatterns.as_view(), name='acl pattern list'),
    url(r'^(?P<id>\d+)/pattern/details/$', AclPatternDetails.as_view(), name='acl pattern details'),
    url(r'^(?P<id>\d+)/pattern/create/$', AclPatternCreate.as_view(), name='acl pattern create'),
    url(r'^(?P<id>\d+)/pattern/update/$', AclPatternUpdate.as_view(), name='acl pattern update'),
    url(r'^(?P<id>\d+)/pattern/delete/$', AclPatternDelete.as_view(), name='acl pattern delete'),
    url(r'^(?P<id>\d+)/delete/$', AclDelete.as_view(), name='acl delete'),
]
