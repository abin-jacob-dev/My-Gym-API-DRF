from django.urls import path
from .views import (
    GymCreateView,
    GymDetailView,
    GymListView,
    PlanListView,
    PlanCreateView,
    PlanDetailView,
    MembershipListView,
    MembershipCreateView,
    MembershipDetailView,
)

urlpatterns = [
    path("", GymListView.as_view(), name="gym_list"),
    path("create/", GymCreateView.as_view(), name="gym_create"),
    path("<int:pk>/", GymDetailView.as_view(), name="gym_detail"),
    #user
    
    # plans
    path("<int:gym_id>/plans/", PlanListView.as_view(), name="plan_list"),
    path("<int:gym_id>/plans/create/", PlanCreateView.as_view(), name="plan_create"),
    path("<int:gym_id>/plans/<int:pk>/", PlanDetailView.as_view(), name="plan_detail"),
    # membership
    path("<int:gym_id>/membership/", MembershipListView.as_view(), name="membership_list"),
    path(
        "<int:gym_id>/membership/create/", MembershipCreateView.as_view(), name="membership_create"
    ),
    path(
        "<int:gym_id>/membership/<int:pk>/", MembershipDetailView.as_view(), name="membership_detail"
    ),
]
