from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Comment
from .models import TranslatorsChat
from .serializers import CommentSerializer
from .serializers import TranslatorsChatSerializer


class CommentViewSet(viewsets.ModelViewSet):
    # Allows access to all requests including unauthenticated ones.
    permission_classes = ()
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TranslatorsChatViewSet(viewsets.ModelViewSet):
    # Allows access to all requests including unauthenticated ones.
    permission_classes = ()
    queryset = TranslatorsChat.objects.all()
    serializer_class = TranslatorsChatSerializer
