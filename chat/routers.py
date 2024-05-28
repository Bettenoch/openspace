from rest_framework import routers
from chat.user.viewsets import UserViewSet
from chat.auth.viewsets.register import RegisterViewSet
from django.urls import path, include

router = routers.SimpleRouter()

############################# USER ###################################

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]