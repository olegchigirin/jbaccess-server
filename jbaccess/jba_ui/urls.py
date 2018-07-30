from django.conf.urls import url

import jba_ui.views.TemplateViews
from . import views

app_name = 'ui'

urlpatterns = [
    # Security urls
    url(r'^$', jba_ui.views.TemplateViews.HomeView.as_view(), name='home'),
    url(r'^security/login/$', views.LoginView.as_view(), name='login'),
    url(r'^security/logout/confirm/$', jba_ui.views.TemplateViews.LogoutConfirmView.as_view(), name='logout confirm'),
    url(r'^security/logout/$', views.LogoutView.as_view(), name='logout'),

    # Person urls
    url(r'^person/$', views.PersonListView.as_view(), name='person list'),
    url(r'^person/(?P<id>\d+)/$', views.PersonDetailView.as_view(), name='person details'),
    url(r'^person/create/$', views.PersonCreateView.as_view(), name='create person'),
    url(r'^person/(?P<id>\d+)/update/$', views.PersonUpdateView.as_view(), name='update person'),
    url(r'^person/(?P<id>\d+)/delete/$', views.PersonDeleteView.as_view(), name='delete person'),

    # Key urls
    url(r'^key/$', views.KeyListView.as_view(), name='key list'),
    url(r'^key/create/$', views.KeyCreateView.as_view(), name='key create'),
    url(r'^key/(?P<id>\d+)/$', views.KeyDetailView.as_view(), name='key details'),
    url(r'^key/(?P<id>\d+)/update/$', views.KeyUpdateView.as_view(), name='key update'),
    url(r'^key/(?P<id>\d+)/delete/$', views.KeyDeleteView.as_view(), name='key delete'),
    url(r'^key/(?P<id>\d+)/attached/$', views.KeyAttachedToPersonView.as_view(), name='attached keys'),

    # Roles urls
    url(r'^role/$', views.RoleListView.as_view(), name='role list'),
    url(r'^role/create/$', views.RoleCreateView.as_view(), name='role create'),
    url(r'^role/(?P<id>\d+)/$', views.RoleDetailView.as_view(), name='role details'),
    url(r'^role/(?P<id>\d+)/update/$', views.RoleUpdateView.as_view(), name='role update'),
    url(r'^role/(?P<id>\d+)/delete/$', views.RoleDeleteView.as_view(), name='role delete'),
]
