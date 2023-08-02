from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Team


class PublicPersonSerializer(serializers.Serializer):
    """
    Serializer for public person data (used for users).
    """

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class PublicTasksSerializer(serializers.Serializer):
    """
    Serializer for public task data.
    """

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    assignees = PublicPersonSerializer(read_only=True, many=True)
    start_date = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField(read_only=True)
    status = serializers.DateTimeField(read_only=True)


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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom TokenObtainPairSerializer with additional claims.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration (create user).
    """

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'password2'
        ]

    def create(self, validated_data):
        """
        Create a new user using the validated data.
        """
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        """
        Validate the password and password2 fields to ensure they match.
        """
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords must match')
        return attrs
