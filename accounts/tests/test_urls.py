from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import UserRegisterApiView, UserLoginView, LogOutAPIView


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('api-accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterApiView)

    def test_login_url_is_resolved(self):
        url = reverse('api-accounts:login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('api-accounts:logout')
        self.assertEqual(resolve(url).func.view_class, LogOutAPIView)
