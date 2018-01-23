from rest_framework import serializers
from .models import Comment, TranslatorsChat, Term


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
        fields = ('id', 'slug', 'pali_set', 'meaning_set', 'comment_set')
        depth = '1'


class TermListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('id', 'slug')
        depth = 1
