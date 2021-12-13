from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme shahbazi',
            age='21',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='sahar',
            password='789654',
            email='sahar@gmail.com',
            full_name='sahar sharifi',
            age='15')

    def test_users_listed(self):
        url = reverse('admin:accounts_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        url = reverse('admin:accounts_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)





















