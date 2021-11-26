from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'age', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_admin': {'read_only': True},
        }
