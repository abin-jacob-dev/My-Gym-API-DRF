from rest_framework import serializers
from .models import Gym, Membership, Plan


class GymSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"
