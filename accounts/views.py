from django.contrib.auth import get_user_model

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
        teamate_emails = self.request.data.get('teamate_emails')
        teamate_emails = teamate_emails.split(',')
        
        teamates = [user]
        for email in teamate_emails:
            try:
                app_user = get_user_model().objects.get(email=email.strip())
                teamates.append(app_user)
            except get_user_model().DoesNotExist:
                pass

        return serializer.save(assigner=user, teamates=teamates)
