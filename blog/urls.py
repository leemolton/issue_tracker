from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.views.static import serve
from checkout import urls as urls_checkout
from .settings import MEDIA_ROOT
from . import views
from .views import index, home, diary, predict, henry, jose
from checkout import views as checkout_views
from checkout.views import predict

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^diary/$', views.diary, name="diary"),
    url(r'^henry/$', henry, name="henry"),
    url(r'^jose/$', jose, name="jose"),
    url(r'^predict/', checkout_views.predict),
    url(r'checkout/', include('checkout.urls')),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
]


