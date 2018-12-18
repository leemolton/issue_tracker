from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.views.static import serve
from checkout import urls as urls_checkout
from .settings import MEDIA_ROOT
from .views import index, home, view, predict

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home, name="home"),
    path(r'view/', view, name="diary"),
    path(r'predict/', predict, name="predict"),
    #path(r'^$', RedirectView.as_view(url='post/')),
    path(r'posts/', include('posts.urls')),
    #path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]


