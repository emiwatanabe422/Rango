from django.urls import path
from rango import views


urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^admin/', admin.site.urls),
]
