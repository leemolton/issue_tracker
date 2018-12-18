from django.conf.urls import url
from django.urls import path
from .views import checkout, pay

urlpatterns = [
    path(r'^$', checkout, name="Checkout"),
    ]