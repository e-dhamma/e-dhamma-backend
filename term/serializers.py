from rest_framework import serializers
from .models import Comment, Term, Pali, Meaning


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class TranslatorsChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TranslatorsChat
#         fields = '__all__'


class MeaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meaning
        fields =  ('id', 'term', 'root', 'rootLang', 'rootDescription', 'expl', 'further', 'est_set', 'eng_set', 'example_set')
        depth = 1


class SingleTermSerializer(serializers.ModelSerializer):
    meaning_set = MeaningSerializer(many=True)
    class Meta:
        model = Term
        fields =  ('id', 'slug', 'pali_set', 'meaning_set', 'comment_set')
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

        """
        Right now the seralizer returns data in wrong format, the correct format should be the following:
        [
            {
            'id' = 1
            'slug' = 'string'
            'pali' = []
            'est' = []
            }
        ]
        """
