from django.shortcuts import render
from .serializers import GymSerilalizer, PlanSerializer, MembershipSerializer
from rest_framework import generics
from .models import Gym, Plan, Membership
from rest_framework.permissions import AllowAny
from accounts.permissions import IsGymOwner
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class GymListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerilalizer
    permission_classes = [AllowAny]


class GymCreateView(generics.CreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerilalizer
    permission_classes = [IsAuthenticated]


class GymDetailView(generics.RetrieveAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerilalizer
    permission_classes = [AllowAny]


class PlanListView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [AllowAny]


class PlanCreateView(generics.CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated, IsGymOwner]


class PlanDetailView(generics.RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [AllowAny]


class MembershipListView(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]


class MembershipCreateView(generics.CreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]


class MembershipDetailView(generics.RetrieveAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]
