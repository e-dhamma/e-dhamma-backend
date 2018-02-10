from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import LetterToAdmin

class LetterToAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterToAdmin
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'groups')