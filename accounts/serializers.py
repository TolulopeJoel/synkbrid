from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Team


class PublicPersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class PublicTasksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    start_date = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField(read_only=True)
    status = serializers.DateTimeField(read_only=True)


class TeamSerializer(serializers.ModelSerializer):
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
