from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from .models import Student

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "phone", "role"]

    def validate(self, data):
        if len(data["password"]) < 8:
            raise serializers.ValidationError("it needs len of 8 character")
        return data

    def validate_phone(self, value):
        if not re.fullmatch(r"[789]\d{9}", value):
            raise serializers.ValidationError(
                "Phone number must  contain exactly 10 digits."
            )
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "role"]
        read_only_fields = ["id", "role"]
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','name','age','place']

        
