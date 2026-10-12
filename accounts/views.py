from django.shortcuts import render
from .models import User
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from .serializers import SignupSerializer, UserSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from accounts.permissions import IsGymOwner

# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "p"


class GymUsersList(ListAPIView):
    permission_classes = [IsGymOwner]
    pagination_class = CustomPagination
    queryset = User.objects.filter(role="member")
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get("search")
        if search:

            queryset = queryset.filter(username__icontains=search)
        return queryset


class SignupView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user is None:
                return Response(
                    {"error": "Invalid username or password."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                }
            )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(
        self,
        request,
    ):
        request.user.auth_token.delete()
        return Response(
            {"message": "Logged Out Successfully"}, status=status.HTTP_200_OK
        )


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
