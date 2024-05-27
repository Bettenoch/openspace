from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from chat.user.serializers import UserSerializer
from chat.user.models import User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
