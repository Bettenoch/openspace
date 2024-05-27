from rest_framework import serializers

from chat.user.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'created', 'updated')
        read_only_field = ['is_active']