from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    CustomTokenObtainPairSerializer,
    RegisterUserSerializer
)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain view that uses CustomTokenObtainPairSerializer.
    """
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    View to register new users with RegisterUserSerializer.
    """
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]
