from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .mixins import UserTeamQueryset
from .models import Team
from .serializers import CustomTokenObtainPairSerializer, TeamSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TeamViewset(UserTeamQueryset, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
