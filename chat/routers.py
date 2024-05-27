from rest_framework import routers
from chat.user.viewsets import UserViewSet
from django.urls import path, include

router = routers.SimpleRouter()

############################# USER ###################################

router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]