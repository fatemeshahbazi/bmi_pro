from rest_framework.test import APITestCase
from core.models import BmiMeasurement


class TestModels(APITestCase):
    def test_creates_BmiMeasurement(self):
        bmi1 = BmiMeasurement.objects.create(height=1.65, weight=70)
        self.assertIsInstance(bmi1, BmiMeasurement)
        self.assertEqual(bmi1.height, 1.65)
        self.assertEqual(bmi1.bmi, 25.71166207529844)
        self.assertEqual(bmi1.weight, 70)
        self.assertEqual(bmi1.result, 'overweight')

    def test_get_bmi(self):
        self.assertEqual(BmiMeasurement.get_bmi(65, 1.65), 23.875114784205696)

    def test_get_result(self):
        self.assertEqual(BmiMeasurement.get_result(23), BmiMeasurement.NORMAL)