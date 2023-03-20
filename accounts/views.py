from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Team
from .serializers import CustomTokenObtainPairSerializer, TeamSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        user_queryset = []

        for team in queryset:
            teamates = team.teamates.all()
            if user in teamates:
                user_queryset.append(team)
        
        return user_queryset
