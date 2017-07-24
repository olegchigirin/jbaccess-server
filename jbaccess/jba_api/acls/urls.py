from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^(?P<id>\d+)$', DeleteAclController.as_view()),
    url(r'^(?P<id>\d+)/patterns$', AclPatternsCRController.as_view()),
    url(r'^patterns/(?P<pattern_id>\d+)$', AclPatternsUDController.as_view())
]
