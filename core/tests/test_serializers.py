from django.test import TestCase
from core.serializers import BmiSerializer
from django.contrib.auth import get_user_model
from core import serializers
from rest_framework.test import APIRequestFactory
from core.models import BmiMeasurement

User = get_user_model()


class SerializerTest(TestCase):
    def setUp(self):
        self.UNDERWEIGHT = 'underweight'
        self.NORMAL = 'normal'
        self.OVERWEIGHT = 'overweight'
        self.OBESE = 'obese'

        self.user = User.objects.create_user(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme shahbazi',
            age='21',
        )

    def test_validate_correct_weight(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.validated_data['weight'], 65)

    def test_validate_correct_height(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        self.assertEqual(serializer.validated_data['height'], 1.65)

    def test_validate_correct_bmi(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data['bmi'], 23.875114784205696)

    def test_validate_correct_bmi_overweight(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '70'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data['bmi'], 25.71166207529844)

    def test_validate_correct_result_overweight(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '70'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data['result'], BmiMeasurement.OVERWEIGHT)

    def test_validate_correct_result_underweight(self):
        data = {
            'user': self.user,
            'height': '165', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data['result'], BmiMeasurement.UNDERWEIGHT)

    def test_validate_correct_result_normal(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data['result'], BmiMeasurement.NORMAL)

    def test_validate_correct_previous_status(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        self.assertEqual(serializer.data['previous_status'], 14.65)

    def test_invalidate_negetive_weight(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '-1'
        }
        serializer = BmiSerializer(data=data)
        self.assertRaises(TypeError, serializer.is_valid())

    def test_invalidate_zero_weight(self):
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '0'
        }
        serializer = BmiSerializer(data=data)
        self.assertRaises(TypeError, serializer.is_valid())
