from django.urls import path
from rest_framework.authtoken import views
from .views import SignupView, LogoutView, ProfileView, GymUsersList, LoginView,StudentListView,StudentUpdateView,StudentCreateView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("users/", GymUsersList.as_view(), name="users"),
    # admin - user delete
    path("students/", StudentListView.as_view(), name="student_list"),
    path("student/", StudentCreateView.as_view(), name="student"),
    path("student/<int:pk>/", StudentUpdateView.as_view(), name="student"),

]
