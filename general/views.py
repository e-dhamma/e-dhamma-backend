from django.shortcuts import render
from rest_framework import viewsets
from .models import LetterToAdmin
from .serializers import LetterToAdminSerializer
from rest_framework.permissions import AllowAny


class LetterToAdminViewSet(viewsets.ModelViewSet):
    permission_classes = () #Allows access to all requests including unauthenticated ones.
    queryset = LetterToAdmin.objects.all()
    serializer_class = LetterToAdminSerializer
