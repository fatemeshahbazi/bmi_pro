from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import BmiCreate


class TestCore(SimpleTestCase):

    def test_bmicreate_url_is_resolved(self):
        url = reverse('core:bmicreate')
        self.assertEqual(resolve(url).func.view_class, BmiCreate)
