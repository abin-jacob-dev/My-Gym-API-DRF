from django.urls import path
from rest_framework.authtoken import views
from .views import SignupView, LogoutView, ProfileView,GymUsersList

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", views.obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("users/", GymUsersList.as_view(), name="users"),

    # admin - user delete
]
