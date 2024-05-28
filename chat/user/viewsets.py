from rest_framework.permissions import AllowAny
from chat.user.serializers import UserSerializer
from chat.user.models import User
from chat.abstract.viewsets import AbstractViewSet

# Create your views here.

class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny,)#change to IsAuthenticated to prevent any user from viewing others
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
