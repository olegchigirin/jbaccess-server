import api_commons.common
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('jba_api.urls')),
]

handler404 = api_commons.common.error_404_handler
handler500 = api_commons.common.error_500_handler
