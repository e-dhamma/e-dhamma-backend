from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Comment, TranslatorsChat, Term
from .serializers import CommentSerializer, TranslatorsChatSerializer, SingleTermSerializer, TermListSerializer


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


class SingleTermViewSet(generics.RetrieveAPIView):
    queryset = Term.objects.all()
    serializer_class = SingleTermSerializer

class TermListViewSet(viewsets.ModelViewSet):
    # Allows access to all requests including unauthenticated ones.
    queryset = Term.objects.all()
    serializer_class = TermListSerializer
