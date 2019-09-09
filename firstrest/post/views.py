from django.shortcuts import render

from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer

# CVB > Class로 view 작성

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer