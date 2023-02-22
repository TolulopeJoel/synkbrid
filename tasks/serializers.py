from rest_framework import serializers

from .models import Task


class AssigneePublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)


class TaskSerializer(serializers.ModelSerializer):
    assignee = AssigneePublicSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = [
            'id',
            'assignee',
            'name',
            'description',
            'start_date',
            'due_date',
            'status',
        ]
        