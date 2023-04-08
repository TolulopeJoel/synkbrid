from rest_framework import serializers

from accounts.serializers import PublicPersonSerializer

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assignees = PublicPersonSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'assignees',
            'start_date',
            'due_date',
            'status',
        ]
