from django.conf.urls import url
from .views import checkout, pay, predict

urlpatterns = [
    url(r'predict/', predict, name="predict"),
    url(r'checkout/', checkout, name="Checkout"),
    ]