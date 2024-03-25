from rest_framework import serializers
from .models import myUser, Post, Comment

class myUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['id', 'email', 'is_active', 'is_staff', 'date_joined']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'content', 'published', 'created_at', 'updated_at', 'status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at', 'status']
