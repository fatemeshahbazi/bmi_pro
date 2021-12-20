from django.test import TestCase, Client
from django.urls import reverse
from core.models import BmiMeasurement
import json
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.test import force_authenticate
from rest_framework import test, status
from core import models
from rest_framework.response import Response


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme shahbazi',
            age='21',
        )

        self.bmimeasurement = BmiMeasurement.objects.create(
            user=self.user,
            height=1.65,
            weight=50,
            bmi=25.71,
            result='OVERWEIGHT'

        )

        self.client = test.APIClient()

    def test_BmiCreate(self):
        bmi = models.BmiMeasurement.objects.create(user=self.user, height=1.65,
                                                   weight=50,
                                                   bmi=25.71,
                                                   result='OVERWEIGHT')

        url = reverse('core:bmicreate')
        token = '35sfdsvsd23#$%#654354fds!fs4'
        self.data = {'height': '1.65', 'weight': '65'}
        response = self.client.post(url, self.data, format='json', HTTP_AUTHORIZATION='token '(token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
