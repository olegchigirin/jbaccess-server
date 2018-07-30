from django.conf.urls import url

from . import views

app_name = 'ui'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^security/login/$', views.LoginView.as_view(), name='login'),
    url(r'^security/logout/confirm/$', views.LogoutConfirmView.as_view(), name='logout confirm'),
    url(r'^security/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^person/$', views.PersonListView.as_view(), name='person list'),
    url(r'^person/(?P<id>\d+)/$', views.PersonDetailView.as_view(), name='person details'),
    url(r'^person/create$', views.PersonCreateView.as_view(), name='create person')
]
