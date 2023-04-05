from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .mixins import UserTeamQueryset
from .models import Team
from .serializers import CustomTokenObtainPairSerializer,RegisterUserSerializer, TeamSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]


class TeamViewset(UserTeamQueryset, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(assigner=user, teamates=[user])
