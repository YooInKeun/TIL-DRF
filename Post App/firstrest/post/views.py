from django.shortcuts import render

from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    queryset = Post.objects.all()
    serializer_class = PostSerializer