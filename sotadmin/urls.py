from django.urls import path
from django.conf.urls.static import static
from . import views

from DAppCentral.settings import common

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    path('', views.sotadmin, name="main"),
    path('index.html', views.sotadmin, name="main"),
    path('wallet.html', views.wallet, name="wallet"),
    path('iot-cat.html', views.iotcat, name="iot-cat"),
    path('iot-cat-detail.html', views.iotcatdetail, name="iot-cat-detail"),
    path('iot-mod-detail.html', views.iotmoddetail, name="iot-mod-detail"),
    path('iot-version.html', views.iotversion, name="iot-version"),
    path('iot-version-detail.html', views.iotversiondetail, name="iot-version-detail"),

] + static(common.STATIC_URL, document_root=common.STATIC_ROOT)
