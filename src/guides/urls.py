from django.urls import path
from .views import guide

urlpatterns = [
    path('<header>', guide),
]