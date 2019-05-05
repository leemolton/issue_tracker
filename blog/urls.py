from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.views.static import serve
from checkout import urls as urls_checkout
from .settings import MEDIA_ROOT
from .views import index, home, view, predict
from checkout import views as checkout_views
from checkout.views import predict

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', home, name="home"),
    url(r'view/', view, name="diary"),
    url(r'henry/', view, name="henry"),
    url(r'jose/', view, name="jose"),
    url(r'^checkout/predict/$', checkout_views.predict),
    url(r'checkout/', include('checkout.urls')),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'posts/', include('posts.urls')),
    #path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]


