from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "phone", "role"]


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "phone", "role"]

    def validate(self, data):
        if len(data["password"]) < 7:
            raise serializers.ValidationError("it needs len of 8 character")
        return data

    def create(self, validated_data):
        User.objects.create_user(**validated_data)
        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "role"]
        read_only_fields = ["id", "date_joined", "role"]
