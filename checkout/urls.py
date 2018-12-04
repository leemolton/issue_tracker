from django.conf.urls import url
from django.urls import path
from .views import checkout

urlpatterns = [
    url(r'^$', checkout, name="Checkout"),
    ]