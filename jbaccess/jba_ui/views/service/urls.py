from django.conf.urls import url

from jba_ui.views.service.ServiceViews import Home, LogoutConfirm, Login, Logout

urlpatterns = [

    url(r'^$', Home.as_view(), name='home'),
    url(r'^security/login/$', Login.as_view(), name='login'),
    url(r'^security/logout/confirm/$', LogoutConfirm.as_view(), name='logout confirm'),
    url(r'^security/logout/$', Logout.as_view(), name='logout'),
]
