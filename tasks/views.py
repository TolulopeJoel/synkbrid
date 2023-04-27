from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.views import Response, status

from accounts.mixins import UserTeamQueryset
from accounts.models import Team

from .models import Task
from .serializers import TaskSerializer


class TaskList(UserTeamQueryset, generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    
    # return tasks for all teams user is in.
    def get_queryset(self):
        queryset = super().get_queryset() # UserTeamQueryset
        user_queryset = []
        
        for team in queryset:
            tasks = team.tasks.all()
            for task in tasks:
                user_queryset.append(task)
        
        return user_queryset
    
    def perform_create(self, serializer):
        team_id = self.request.data.get('team_id')
        assignees_username= self.request.data.get('assignees_username')
        assignees_username = assignees_username.split(',')

        if '' in assignees_username:
            assignees_username.remove('') 

        team = Team.objects.get(id=team_id)
        teamates = team.teamates.all()

        assignees = []
        for username in assignees_username:
            if username == '__all__teamates__':
                assignees = [i for i in teamates]
            else:
                try:
                    user = get_user_model().objects.get(username=username.strip())
                    if user in teamates:
                        assignees.append(user)
                    else:
                        return Response({'detail': 'User in not in Team'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                except get_user_model().DoesNotExist:
                    return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return serializer.save(team=team, assignees=assignees)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
