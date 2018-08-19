from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from jba_ui.views.service.ServiceViews import Home, LogoutConfirm, Login, Logout

urlpatterns = [

    url(r'^$', Home.as_view(), name='home'),
    url(r'^security/login/$', Login.as_view(), name='login'),
    url(r'^security/logout/confirm/$', login_required(LogoutConfirm.as_view()), name='logout confirm'),
    url(r'^security/logout/$', login_required(Logout.as_view()), name='logout'),
]
