from django.conf.urls import url

import jba_ui.views.ServiceViews
from . import views

app_name = 'ui'

urlpatterns = [
    # Security urls
    url(r'^$', jba_ui.views.ServiceViews.HomeView.as_view(), name='home'),
    url(r'^security/login/$', views.LoginView.as_view(), name='login'),
    url(r'^security/logout/confirm/$', jba_ui.views.ServiceViews.LogoutConfirmView.as_view(), name='logout confirm'),
    url(r'^security/logout/$', views.LogoutView.as_view(), name='logout'),

    # Service urls

    url(r'^(?P<id>\d+)/(?P<model_name>\w+)/$', views.DetailRedirectView.as_view(), name='redirect details'),

    # Person urls
    url(r'^person/$', views.PersonListView.as_view(), name='person list'),
    url(r'^person/(?P<id>\d+)/$', views.PersonDetailView.as_view(), name='person details'),
    url(r'^person/create/$', views.PersonCreateView.as_view(), name='person create'),
    url(r'^person/(?P<id>\d+)/update/$', views.PersonUpdateView.as_view(), name='person update'),
    url(r'^person/(?P<id>\d+)/delete/$', views.PersonDeleteView.as_view(), name='person delete'),
    url(r'^person/(?P<id>\d+)/roles', views.AttachedRolesToPersonView.as_view(), name='person attached roles'),

    # Key urls
    url(r'^key/$', views.KeyListView.as_view(), name='key list'),
    url(r'^key/create/$', views.KeyCreateView.as_view(), name='key create'),
    url(r'^key/(?P<id>\d+)/$', views.KeyDetailView.as_view(), name='key details'),
    url(r'^key/(?P<id>\d+)/update/$', views.KeyUpdateView.as_view(), name='key update'),
    url(r'^key/(?P<id>\d+)/delete/$', views.KeyDeleteView.as_view(), name='key delete'),
    url(r'^key/(?P<id>\d+)/attached/$', views.KeyAttachedToPersonView.as_view(), name='key attached to person'),
    url(r'^key/(?P<id>\d+)/attach', views.AttachKeyToPersonView.as_view(), name='key attach'),

    # Roles urls
    url(r'^role/$', views.RoleListView.as_view(), name='role list'),
    url(r'^role/create/$', views.RoleCreateView.as_view(), name='role create'),
    url(r'^role/(?P<id>\d+)/$', views.RoleDetailView.as_view(), name='role details'),
    url(r'^role/(?P<id>\d+)/update/$', views.RoleUpdateView.as_view(), name='role update'),
    url(r'^role/(?P<id>\d+)/delete/$', views.RoleDeleteView.as_view(), name='role delete'),
    url(r'^role/(?P<id>\d+)/attach/$', views.AttachRoleToPersonView.as_view(), name='role attach to person'),
    url(r'^role/(?P<id>\d+)/detach/$', views.DetachRoleFromPersonView.as_view(), name='role detach from person'),

    # Controllers urls
    url(r'^controller/$', views.ControllerListView.as_view(), name='controller list'),
    url(r'^controller/(?P<id>\d+)/$', views.ControllerDetailsView.as_view(), name='controller details'),
    url(r'^controller/create', views.ControllerCreateView.as_view(), name='controller create'),
    url(r'^controller/(?P<id>\d+)/update$', views.ControllerUpdateView.as_view(), name='controller update'),
    url(r'^controller/(?P<id>\d+)/delete$', views.ControllerDeleteView.as_view(), name='controller delete'),

    # Doors urls
    url(r'^door/$', views.DoorListView.as_view(), name='door list'),
    url(r'^door/(?P<id>\d+)/$', views.DoorDetailsView.as_view(), name='door details'),
    url(r'^door/create', views.DoorCreateView.as_view(), name='door create'),
    url(r'^door/(?P<id>\d+)/update$', views.DoorUpdateView.as_view(), name='door update'),
    url(r'^door/(?P<id>\d+)/delete$', views.DoorDeleteView.as_view(), name='door delete'),

    # Places urls
    url(r'^place/$', views.PlaceListView.as_view(), name='place list'),
    url(r'^place/(?P<id>\d+)/$', views.PlaceDetailsView.as_view(), name='place details'),
    url(r'^place/create', views.PlaceCreateView.as_view(), name='place create'),
    url(r'^place/(?P<id>\d+)/update$', views.PlaceUpdateView.as_view(), name='place update'),
    url(r'^place/(?P<id>\d+)/delete$', views.PlaceDeleteView.as_view(), name='place delete'),
]
