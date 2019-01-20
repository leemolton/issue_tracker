from django.conf.urls import url
from django.urls import path
from .views import checkout, pay, predict

urlpatterns = [
    path(r'predict/', predict, name="predict"),
    path(r'checkout/', checkout, name="Checkout"),
    ]