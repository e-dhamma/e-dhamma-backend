from rest_framework import routers
from general.views import LetterToAdminViewSet

router = routers.DefaultRouter()
router.register('letter-to-admin', LetterToAdminViewSet)