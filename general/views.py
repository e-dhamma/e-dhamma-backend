from django.shortcuts import render
from rest_framework import viewsets
from .models import LetterToAdmin
from .serializers import LetterToAdminSerializer

class LetterToAdminViewSet(viewsets.ModelViewSet):
    queryset = LetterToAdmin.objects.all()
    serializer_class = LetterToAdminSerializer

