from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import Response, status

from accounts.mixins import UserTeamQueryset
from accounts.models import Team

from .models import Task
from .serializers import TaskSerializer


class TaskList(UserTeamQueryset, generics.ListCreateAPIView):
    """
    API view to list and create tasks for all teams the user is in.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Return the queryset containing tasks for all teams the user is in.
        """
        queryset = super().get_queryset()  # UserTeamQueryset
        return Task.objects.filter(team__in=queryset)

    def perform_create(self, serializer):
        """
        Create a new task for a specified team and assignees.
        """
        team_id = self.request.data.get('team_id')
        assignees_username = self.request.data.get(
            'assignees_username', '').split(',')
        assignees_username = [
            username.strip() for username in assignees_username.split(',') if username.strip()
        ]

        # Get the team object or return a 404 response if the team does not exist.
        team = get_object_or_404(Team, id=team_id)
        teamates = team.teamates.all()

        assignees = []
        for username in assignees_username:

            if username == '__all__teamates__':
                # Add all teamates to assignees list when '__all__teamates__' is provided.
                assignees.extend(teamates)
            else:
                # Get the user object or return a 404 response if the user does not exist.
                user = get_object_or_404(get_user_model(), username=username)

                if user in teamates:
                    assignees.append(user)
                else:
                    # Return a 406 response if the user is not in the team.
                    return Response({'detail': 'User is not in Team'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # Save the task with the specified team and assignees.
        serializer.save(team=team, assignees=assignees)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
