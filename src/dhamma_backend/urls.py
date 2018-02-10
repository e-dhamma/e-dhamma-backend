"""dhamma_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from general.api.views import LetterToAdminViewSet, UserViewSet, UserLoginAPIView
from general.views import homepage
from term.api.views import CommentViewSet, SingleTermViewSet, TermListViewSet

router = routers.DefaultRouter()

router.register('letter-to-admin', LetterToAdminViewSet)
router.register('term-comment', CommentViewSet)
router.register('term-list', TermListViewSet)
# router.register('translators-chat', TranslatorsChatViewSet)


urlpatterns = [
    path('', homepage),
    path('api/', include(router.urls)),
    path('api/single-term/<str:slug>/', SingleTermViewSet.as_view()),
    path('api/users/<str:username>', UserViewSet.as_view()),
    path('api/login/', UserLoginAPIView.as_view()),
    path('haldus/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('juhendid/', include('guides.urls'))
]
