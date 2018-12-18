from django.conf.urls import url
from django.urls import path
from .views import add, get_posts, post_detail, new_post


urlpatterns = [
    path(r'add/', add, name="add"),
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new_post/$', new_post, name='new_post'),
    #url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]