from django.test import TestCase
from core.serializers import BmiSerializer
from django.contrib.auth import get_user_model
from core import serializers
from rest_framework.test import APIRequestFactory

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
        rf = APIRequestFactory()

    def test_validate_correct_weight(self):
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(request=request, data=data)
        serializer.is_valid()
        self.assertEqual(serializer.validated_data['weight'], 65)

    def test_validate_correct_height(self):
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(request=request, data=data)
        serializer.is_valid()
        self.assertEqual(serializer.validated_data['height'], 1.65)

    # def test_validate_correct_bmi(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {
    #         'user': self.user,
    #         'height': '1.65', 'weight': '65'
    #     }
    #     serializer = BmiSerializer(request=request, data=data)
    #     self.assertEqual(serializer.validated_data['bmi'], 23.78)
    #
    def test_validate_correct_previous_status(self):
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        data = {
            'user': self.user,
            'height': '1.65', 'weight': '65'
        }
        serializer = BmiSerializer(request=request, data=data)
        serializer.is_valid()
        print(serializer.validated_data)
        self.assertEqual(serializer.validated_data['previous_status'], 'You need to lose 8.98 kgs')

    # def test_invalidate_negetive_weight(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {
    #         'user': self.user,
    #         'height': '1.65', 'weight': '0'
    #     }
    #     serializer = BmiSerializer(request=request, data=data)
    #     self.assertFalse(serializer.is_valid())
    #     self.assertRaises(serializer.validated_data['weight'])
    #
    # def test_invalidate_zero_weight(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {
    #         'user': self.user,
    #         'height': '1.65', 'weight': '0'
    #     }
    #     serializer = BmiSerializer(request=request, data=data)
    #     self.assertFalse(serializer.is_valid())
    #     self.assertRaises(serializer.validated_data['weight'])

    def test_invalidate_negetive_height(self):
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        data = {
            'user': self.user,
            'height': '-10', 'weight': '65'
        }
        serializer = BmiSerializer(request=request, data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_zero_height(self):
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        data = {
            'user': self.user, 'height': '0', 'weight': '65'
        }
        serializer = BmiSerializer(request=request, data=data)
        self.assertFalse(serializer.is_valid())






    #
    # def test_invalidate_negetive_weight(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {'user':self.user, 'height':'1.65', 'weight':'-2', 'bmi':'0', 'previous_status': 'you are underweight'}
    #     serializer = BmiSerializer(request=request, data=data)
    #     serializer.is_valid()
    #     self.assertEqual(serializer.validated_data['weight'], 1)
    #     # self.assertRaises(ValueError)
    #
    #
    #
    # def test_validate_height(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {'height': '1.65'}
    #     serializer = BmiSerializer(request=request, data=data)
    #     serializer.is_valid()
    #     self.assertEqual(serializer.validate_height(1.60), 1.70)
    #     # self.assertEqual(serializer.validate_height(1.60), 1.60)
    #
    #
    # def test_get_bmi(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {'height': '1.7', 'weight': '60'}
    #     serializer = BmiSerializer(request=request, data=data)
    #     serializer.is_valid()
    #     self.assertEqual(serializer.get_bmi(60, 1.7), 20.761245674740486)
    #     # self.assertEqual(serializer.get_bmi(45, 1.80), 13.09)
    #     # self.assertEqual(serializer.get_bmi(87, 1.70), 26.85)
    #
    # def test_get_delta_weight(self, height, weight):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #
    #
    # def test_get_result(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     data = {'bmi': '20',}
    #     serializer = BmiSerializer(request=request, data=data)
    #     BmiSerializer.bmi == 20
    #     self.assertEqual(serializer.get_result(), self.OBESE)
    #
    # def test_valid_data(self):
    #     data = {
    #         'user': self.user,
    #         'height': '1.65', 'weight': '65', 'bmi': '23.78', 'previous_status': '8.98'
    #     }
    #     factory = APIRequestFactory()
    #     request = factory.get('127.0.0.0:8000/bmi')
    #     serializer = BmiSerializer(request=request, data=data)
    #     self.assertTrue(serializer.is_valid())
    #
    def test_invalid_data(self):
        data = {
            'height': '1.65',
        }
        factory = APIRequestFactory()
        request = factory.get('127.0.0.0:8000/bmi')
        serializer = BmiSerializer(request=request, data=data)
        self.assertFalse(serializer.is_valid())
