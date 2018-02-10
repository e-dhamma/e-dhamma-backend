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

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        password = data['password']
        if not username:
            raise serializers.ValidationError('Username is required.')

        user = User.objects.filter(username=username)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect credentials.')
        data['token'] = 'A hardcoded token'
        return data