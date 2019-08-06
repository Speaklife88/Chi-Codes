from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.lr_app.routes')),
    url(r'^wall/', include('apps.RF_app.routes')),
]
