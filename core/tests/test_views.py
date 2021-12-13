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

        # url = reverse('core:bmicreate')
        # self.data ='token 35sfdsvsd23#$%#654354fds!fs4'
        # # Create a user is a workaround in order to authentication works
        #
        # # First post to get token
        # response = self.client.post(url, self.data, format='json')
        #
        # request = self.client.post(reverse('core:bmicreate'), {'user': self.user, 'height': '1.65',
        #                                                        'weight': '50'})
        # # context = {'bmi': '25.71', 'result': 'OVERWEIGHT', 'previous_status': 'You need to lose 6.53kgs'}
        # print(request.status_code)
        # self.assertTrue(request.status_code == status.HTTP_200_OK)
        #
        # # self.assertIn('25.71', Response.content)

        # token = '35sfdsvsd23#$%#654354fds!fs4'
        # print(token)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' +token)
        # response = self.client.get(reverse('core:bmicreate'), headers={'Authorization': 'Token ' +token},
        #                            data={'format': 'json'})
        # print(response)

        # ....
        # self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        # # Next post/get's will require the token to connect
        # self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        # response = self.client.get(reverse('core:bmicreate'), data={'format': 'json'})
        # print(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
#
# # Include an appropriate `Authorization:` header on all requests.
# # token = Token.objects.get(user__username=self.clark_user.username)
# client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
#
# response = client.patch(self.url_people, serializer.data, format='json')
# self.assertEqual(response.status_code, status.HTTP_200_OK)
# client.logout()
# TEST_USER = {
#     'username' : 'sahar', 'email' :'sahar@mail.com', 'password':'789654', 'full_name' : 'sahar taheri', 'age' :'23'
# }
# BASE_URL = 'http://127.0.0.1:8000/accounts/login'
# API_LOGIN = 'http://127.0.0.1:8000/accounts/login' + 'api-token-auth/'
#
#
# class TestAuthentication(TestCase):
#     def setUp(self):
#         get_user_model().objects.create(**TEST_USER)
#         self.requests = RequestsClient()
#
#     def test_user_can_login(self):
#         user = get_user_model().objects.first()
#         self.assertEqual(get_user_model().objects.count(), 1)
#         response = self.requests.post(API_LOGIN, TEST_USER)
#         print(response.content)
