from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .ACLsViews import AclPatternDetails, AclPatternCreate, AclPatterns, AclPatternUpdate, AclPatternDelete, AclDelete

urlpatterns = [
    url(r'^(?P<id>\d+)/$', login_required(AclPatterns.as_view()), name='acl pattern list'),
    url(r'^(?P<id>\d+)/pattern/details/$', login_required(AclPatternDetails.as_view()), name='acl pattern details'),
    url(r'^(?P<id>\d+)/pattern/create/$', login_required(AclPatternCreate.as_view()), name='acl pattern create'),
    url(r'^(?P<id>\d+)/pattern/update/$', login_required(AclPatternUpdate.as_view()), name='acl pattern update'),
    url(r'^(?P<id>\d+)/pattern/delete/$', login_required(AclPatternDelete.as_view()), name='acl pattern delete'),
    url(r'^(?P<id>\d+)/delete/$', login_required(AclDelete.as_view()), name='acl delete'),
]
