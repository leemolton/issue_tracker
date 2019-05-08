from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from blog import urls as urls_blog
from blog import views as v
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', v.index),
    url(r'^blog/', include( include('blog.urls')),
    url(r'^/checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    
]
