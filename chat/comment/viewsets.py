from django.http.response import Http404

from rest_framework.response import Response
from rest_framework import status
from chat.abstract.viewsets import AbstractViewSet
from chat.comment.models import Comment
from chat.comment.serializers import CommentSerializer
from chat.auth.permissions import UserPermission

# Create your views here.
class CommentViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (UserPermission,)
    serializer_classes = CommentSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            return Http404
        queryset = Comment.objects.filter(post__public_id=post_pk)
        
        return queryset
    
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        
        return obj
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)