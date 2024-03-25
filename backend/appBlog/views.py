from rest_framework import viewsets, permissions
from .models import myUser, Post, Comment
from .serializers import myUserSerializer, PostSerializer, CommentSerializer

# ViewSets define the view behavior.

class myUserViewSet(viewsets.ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = myUserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
