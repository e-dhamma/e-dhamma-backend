from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer
from rest_framework.permissions import AllowAny

from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = () #Allows access to all requests including unauthenticated ones.
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
