from django.conf.urls import url, include

import jba_ui.views.service.ServiceViews
from . import views

app_name = 'ui'

urlpatterns = [

    url(r'^', include('jba_ui.views.service.urls')),
    url(r'^person/+', include('jba_ui.views.personnel.urls')),
    url(r'^key/+', include('jba_ui.views.key.urls')),
    url(r'^role/+', include('jba_ui.views.role.urls')),
    url(r'^controller/+', include('jba_ui.views.controller.urls')),
    url(r'^door/+', include('jba_ui.views.door.urls')),
    url(r'^places/+', include('jba_ui.views.place.urls')),
]
