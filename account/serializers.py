from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    gender = serializers.ChoiceField(choices=User.GENDER, required=True)
    password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'gender', 'password', 'password1')

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password1']:
            raise serializers.ValidationError('Password does not match password1.')
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        self.user = user
        return validated_data