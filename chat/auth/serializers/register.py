from rest_framework import serializers

from chat.user.serializers import UserSerializer
from chat.user.models import User


class RegisterSerializer(UserSerializer):
    # Register serializer for requests and user creation

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        # List all the fields that can be included in a request or response
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "username",
        ]

    def create(self, validated_data):
        # Create a new user with encrypted password and return it
        return User.objects.create_user(**validated_data)
