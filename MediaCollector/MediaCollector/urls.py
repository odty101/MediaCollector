from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^movies/', include('Movies.urls')),
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls'))
]
