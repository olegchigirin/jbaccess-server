from django.conf.urls import url

from jba_ui.views.key.KeyViews import KeyList, KeyCreate, KeyDetail, KeyUpdate, KeyDelete

urlpatterns = [
    url(r'^$', KeyList.as_view(), name='key list'),
    url(r'^create/$', KeyCreate.as_view(), name='key create'),
    url(r'^(?P<id>\d+)/$', KeyDetail.as_view(), name='key details'),
    url(r'^(?P<id>\d+)/update/$', KeyUpdate.as_view(), name='key update'),
    url(r'^(?P<id>\d+)/delete/$', KeyDelete.as_view(), name='key delete'),
]
