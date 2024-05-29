from chat.abstract.serializers import AbstractSerializer

from chat.user.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "bio",
            "avatar",
            "first_name",
            "last_name",
            "is_active",
            "created",
            "updated",
        ]

        read_only_field = ["is_active"]
