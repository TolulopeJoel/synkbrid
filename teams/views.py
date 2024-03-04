from django.contrib.auth import get_user_model

from rest_framework.viewsets  import ModelViewSet

from .mixins import UserTeamQueryset
from .models import Team
from .serializers import TeamSerializer


class TeamViewset(UserTeamQueryset, ModelViewSet):
    """
    Viewset to handle CRUD operations for Team model.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        """
        Custom create method for Team instances.
        """
        user = self.request.user
        teamate_emails = self.request.data.get('teamate_emails', '').split(',')
        teamate_emails = [
            email.strip() for email in teamate_emails if email.strip()
        ]

        # Get the existing users matching the provided email addresses
        existing_users = get_user_model().objects.filter(email__in=teamate_emails)

        # Combine the current user and existing users as team members
        teamates = [user] + list(existing_users)

        # Save the team with the assigner (current user) and team members
        serializer.save(assigner=user, teamates=teamates)
