from rest_framework import serializers
from .models import Comment
from .models import TranslatorsChat

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TranslatorsChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorsChat
        fields = '__all__'