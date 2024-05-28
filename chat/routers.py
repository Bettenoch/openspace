from rest_framework import routers
from chat.user.viewsets import UserViewSet
from chat.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from django.urls import path, include

router = routers.SimpleRouter()

############################# USER ###################################

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
    *router.urls,
]