from chat.user.viewsets import UserViewSet
from chat.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from chat.post.viewsets import PostViewSet
from chat.comment.viewsets import CommentViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()

############################# USER ###################################

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'post', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *posts_router.urls,
]