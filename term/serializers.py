from rest_framework import serializers
from .models import Term, Meaning, Comment, Example


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class TranslatorsChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TranslatorsChat
#         fields = '__all__'


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'original', 'translation')
        depth = 1


class MeaningSerializer(serializers.ModelSerializer):
    example_set = ExampleSerializer(many=True)

    class Meta:
        model = Meaning
        fields = ('id', 'est', 'eng', 'root', 'rootLang',
                  'rootDescription', 'expl', 'further', 'example_set')
        depth = 1


class SingleTermSerializer(serializers.ModelSerializer):
    meaning_set = MeaningSerializer(many=True)

    class Meta:
        model = Term
        fields = ('id', 'slug', 'pali', 'wordClass', 'gender', 'meaning_set', 'comment_set')
        depth = 1


class MeaningForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meaning
        fields = ('est', 'eng')


class TermListSerializer(serializers.ModelSerializer):
    meaning_set = MeaningForListSerializer(many=True)

    class Meta:
        model = Term
        fields = ('id', 'slug', 'pali', 'meaning_set')
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
