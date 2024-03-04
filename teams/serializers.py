from rest_framework import serializers

from accounts.serializers import PublicPersonSerializer, PublicTasksSerializer


from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for Team model data.
    """

    assigner = PublicPersonSerializer(read_only=True)
    teamates = PublicPersonSerializer(read_only=True, many=True)
    tasks = PublicTasksSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'assigner',
            'tasks',
            'teamates',
        ]