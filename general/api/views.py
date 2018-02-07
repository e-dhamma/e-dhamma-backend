from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import LetterToAdmin
from .serializers import LetterToAdminSerializer


class LetterToAdminViewSet(viewsets.ModelViewSet):
    # Allows access to all requests including unauthenticated ones.
    permission_classes = ()
    queryset = LetterToAdmin.objects.all()
    serializer_class = LetterToAdminSerializer
