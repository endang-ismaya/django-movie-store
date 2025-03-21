from django.urls import path

from apps.account import views

urlpatterns = [
    path("signup/", views.signup, name="accounts.signup"),
    path("login/", views.login, name="accounts.login"),
    path("logout/", views.logout, name="accounts.logout"),
]
