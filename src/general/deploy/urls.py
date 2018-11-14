from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:deploy_key>/', views.deploy),
]
