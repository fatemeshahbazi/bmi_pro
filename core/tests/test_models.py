from rest_framework.test import APITestCase
from core.models import BmiMeasurement


class TestModels(APITestCase):
    def test_creates_BmiMeasurement(self):
        bmi1 = BmiMeasurement.objects.create(height=1.65, weight=70, bmi=25.71, result='OVERWEIGHT')
        self.assertIsInstance(bmi1, BmiMeasurement)
        self.assertEqual(bmi1.height, 1.65)
        self.assertEqual(bmi1.bmi, 25.71)
        self.assertEqual(bmi1.weight, 70)
        self.assertEqual(bmi1.result, 'OVERWEIGHT')

