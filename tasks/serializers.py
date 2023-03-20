from rest_framework import serializers

from .models import Task

from accounts.serializers import TeamSerializer


class TaskSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'team',
            'description',
            'start_date',
            'due_date',
            'status',
        ]
        