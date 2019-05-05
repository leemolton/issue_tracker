from django.conf.urls import url
#from django.urls import path
from .views import get_posts, add_comment, post_detail,  new_post, edit_post


urlpatterns = [
    url(r'^$', get_posts, name="get_posts"),
    url(r'^(?P<pk>\d+)/add_comment/$', add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', new_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_post, name='edit_post')
]