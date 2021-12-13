from django.test import TestCase
from accounts.models import User
from rest_framework.test import APITestCase
from accounts.models import User


class TestModels(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user(full_name='hani taghavi', age='20',
                                        email='hani@gmail.com', username='sahel20', password='1458'
                                        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'hani@gmail.com')
        self.assertFalse(user.is_staff)

    def test_creates_superuser(self):
        user = User.objects.create_superuser(full_name='sahael', age='20',
                                             email='sahel@gmail.com', username='sahel20', password='146')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'sahel@gmail.com')
        self.assertTrue(user.is_staff)

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(TypeError, User.objects.create_user, email='hani@gmail.com', password='1458', age='20',
                          full_name='hani taghavi')
        self.assertRaisesMessage(TypeError, 'full_name is required')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(TypeError, User.objects.create_user, username='sahel20', password='1458', age='20',
                          full_name='hani taghavi')
        self.assertRaisesMessage(TypeError, 'email is required')

    def test_raises_error_when_no_age_is_supplied(self):
        self.assertRaises(TypeError, User.objects.create_user, email='hani@gmail.com', password='1458',
                          username='sahel20', full_name='hani taghavi')
        self.assertRaisesMessage(TypeError, 'age is required')

    def test_raises_error_when_no_full_name_is_supplied(self):
        self.assertRaises(TypeError, User.objects.create_user, email='hani@gmail.com', password='1458',
                          username='sahel20', age='20')
        self.assertRaisesMessage(TypeError, 'full_name is required')

    def test_raises_error_superuser_with_is_staff_status(self):
        self.assertRaises(TypeError, User.objects.create_superuser, full_name='hani taghavi', email='hani@gmail.com',
                          password='1458',
                          username='sahel20', age='20', is_staff=False)
        self.assertRaisesMessage(TypeError, 'is_staff must be True')

    def test_raises_error_superuser_with_is_superuser_status(self):
        self.assertRaises(TypeError, User.objects.create_superuser, full_name='hani taghavi', email='hani@gmail.com',
                          password='1458',
                          username='sahel20', age='20', is_superuser=False)
        self.assertRaisesMessage(TypeError, 'is_sup must be True')
