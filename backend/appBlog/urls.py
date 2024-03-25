from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import myUserViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('users', myUserViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
