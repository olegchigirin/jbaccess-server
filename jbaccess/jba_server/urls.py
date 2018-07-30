import api_commons.common
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('jba_api.urls')),
    url(r'^admin/?', admin.site.urls),
    url(r'^accounts/?', include('django.contrib.auth.urls')),
    url(r'^jbaccess/?', include('jba_ui.urls'))
]

handler404 = api_commons.common.error_404_handler
handler500 = api_commons.common.error_500_handler
