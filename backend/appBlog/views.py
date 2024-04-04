from rest_framework import viewsets, status
from .models import myUser, Post, Comment
from .serializers import myUserSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# ViewSets define the view behavior.

# ViewSets for managing the users
# myUserViewSet is used to view all the users
class myUserViewSet(viewsets.ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = myUserSerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

# APIView for create a new user
class CreateUserViewSet(APIView):
    pass

# APIView for login a user
class LoginUserViewSet(APIView):
    pass

# APIView for logout a user
class LogoutUserViewSet(APIView):
    pass

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
