from rest_framework import serializers
from .models import Comment, TranslatorsChat, Term, Pali


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
        depth = 2

class PaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pali
        fields = ('pali',)

class TermListSerializer(serializers.ModelSerializer):
    pali_set = PaliSerializer(many=True)
    class Meta:
        model = Term
        fields = ('id', 'slug', 'pali_set')
        # depth = 1

        """ [
            {
            id = 1
            slug = ''
            pali = []
            est = []
            }
        ]"""
