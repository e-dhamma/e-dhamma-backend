from rest_framework import serializers
from .models import Comment
from .models import TranslatorsChat
from .models import Term

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TranslatorsChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorsChat
        fields = '__all__'


class SingleTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'
