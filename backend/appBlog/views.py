from rest_framework import viewsets
from .models import myUser, Post, Comment
from .serializers import myUserSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# ViewSets define the view behavior.

class myUserViewSet(viewsets.ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = myUserSerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
