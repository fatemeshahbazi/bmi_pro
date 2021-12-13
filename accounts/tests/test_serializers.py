from rest_framework.test import APITestCase
from accounts.models import User
from accounts import serializers


class TestUserRegisterSerializer(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme shahbazi',
            age='21',
        )

    def test_valid_data(self):
        data = {
            'username': 'djanjkjkgo',
            'password': '123456',
            'email': 'django@gmail.com',
            'full_name': 'fateme shahbazi',
            'age': '21',

        }
        serializer = serializers.UserRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_invalid_data(self):
        data = {
            'username': 'django',
            'email': 'django@django.com',
            'full_name': 'fateme shahbazi',
            'age': '21',
        }
        serializer = serializers.UserRegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
