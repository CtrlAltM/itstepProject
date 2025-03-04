from django.urls import path
from .views import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
]