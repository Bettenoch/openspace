from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from chat.abstract.serializers import AbstractSerializer
from chat.post.models import Post
from chat.user.models import User
from chat.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset = User.objects.all(), slug_field='public_id')
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You are not the author of this post")
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        
        return rep
    class Meta:
        model = Post
        
        fields = ['id', 'author', 'body', 'created_at', 'updated_at']
        read_only_fields = ["edited"]