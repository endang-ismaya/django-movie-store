from django.urls import path

from apps.home import views

urlpatterns = [
    path("", views.index, name="home.index"),
    path("", views.about, name="home.about"),
]
