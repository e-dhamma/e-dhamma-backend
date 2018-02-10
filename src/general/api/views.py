from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from ..models import LetterToAdmin
from .serializers import LetterToAdminSerializer, UserSerializer


class LetterToAdminViewSet(viewsets.ModelViewSet):
    # Allows access to all requests including unauthenticated ones.
    permission_classes = ()
    queryset = LetterToAdmin.objects.all()
    serializer_class = LetterToAdminSerializer

class UserViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
