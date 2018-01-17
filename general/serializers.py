from rest_framework import serializers
from .models import LetterToAdmin

class LetterToAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterToAdmin
        fields = '__all__'