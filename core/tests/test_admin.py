from django.test import TestCase, Client
from core.models import BmiMeasurement
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import User


class AdminSiteTest(TestCase):

    def setUp(self):
        self.bmi = BmiMeasurement.objects.create(
            height=1.65, weight=70, bmi=25.71, result='OVERWEIGHT')

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme shahbazi',
            age='21',
        )
        self.client.force_login(self.admin_user)

    def test_bmimeasurement_listed(self):
        url = reverse('admin:core_bmimeasurement_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.bmi.height)
        self.assertContains(res, self.bmi.weight)
