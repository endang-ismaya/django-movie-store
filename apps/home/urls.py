from django.urls import path

from apps.home import views

urlpatterns = [
    path("", views.index, name="home.index"),
    path("about/", views.about, name="home.about"),
]
