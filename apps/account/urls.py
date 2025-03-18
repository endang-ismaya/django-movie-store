from django.urls import path

from apps.account import views

urlpatterns = [
    path("signup/", views.signup, name="accounts.signup"),
]
