from django.conf.urls import url, include

urlpatterns = [
    url(r'^heartbeat/?', include('jba_api.heartbeat.urls')),
    url(r'^calc/?', include('jba_api.calculator.urls')),
    url(r'^security/?', include('jba_api.security.urls'))
]
