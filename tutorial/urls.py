from django.conf.urls import url, include
from django.contrib import admin
from tutorial import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls')),
    url(r'^$',views.girise_yonlendir, name='girise_yonlendir'),
]
