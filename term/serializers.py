from rest_framework import serializers
from general.models import LetterToAdmin

class LetterToAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterToAdmin
        fields = '__all__'