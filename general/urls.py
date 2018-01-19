from rest_framework import routers
from general.views import LetterToAdminViewSet
from term.views import CommentViewSet

router = routers.DefaultRouter()
router.register('letter-to-admin', LetterToAdminViewSet)
router.register('term-comment', CommentViewSet)