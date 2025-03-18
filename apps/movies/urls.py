from django.urls import path

from apps.movies import views

urlpatterns = [
    path("", views.index, name="movies.index"),
    path("<int:id>", views.show, name="movies.show"),
]
