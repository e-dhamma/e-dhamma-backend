from rest_framework import routers
from .views import CommentViewSet
from general.views import router

router = routers.DefaultRouter()
router.register('term-comment', CommentViewSet)