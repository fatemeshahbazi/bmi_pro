from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'age', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_admin': {'read_only': True},
        }

    def validate(self, attrs):
        username = attrs.get('username', '')
        email = attrs.get('email', '')
        age = attrs.get('age', '')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Username is already exists')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email is already exists')})
        if age <= 0:
            raise serializers.ValidationError({'age': 'Age can not be zero or less'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_admin': {'read_only': True},
        }


