# This is my views.py file
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("prices/", views.prices, name="prices"),
]
