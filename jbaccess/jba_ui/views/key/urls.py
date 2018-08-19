from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.key.KeyViews import KeyList, KeyCreate, KeyDetail, KeyUpdate, KeyDelete

urlpatterns = [
    url(r'^$', login_required(KeyList.as_view()), name='key list'),
    url(r'^create/$', login_required(KeyCreate.as_view()), name='key create'),
    url(r'^(?P<id>\d+)/$', login_required(KeyDetail.as_view()), name='key details'),
    url(r'^(?P<id>\d+)/update/$', login_required(KeyUpdate.as_view()), name='key update'),
    url(r'^(?P<id>\d+)/delete/$', login_required(KeyDelete.as_view()), name='key delete'),
]
