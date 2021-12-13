import json
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

User = get_user_model()
from django.contrib import auth
from rest_framework_jwt.settings import api_settings
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import jwt

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from django.contrib.auth import settings


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com',
            full_name='fateme adw',
            age='21',
        )

    def test_register_valid_POST(self):
        request = self.client.post(reverse('api-accounts:register'), {
            'username': 'sahar',
            'password': '789654',
            'email': 'sahar@gmail.com',
            'full_name': 'sahar sharifi',
            'age': '15'
        })

        self.assertEqual(request.status_code, 201)

    def test_register_invalid_POST(self):
        request = self.client.post(reverse('api-accounts:register'), {
            'username': '****',
            'email': 'django',
            'password': '',
            'email': 'abcd',
            'full_name': 'abcd',
            'age': -1

        })
        self.assertEqual(request.status_code, 400)


class AuthViewsTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'sahar'
        self.password = '789654'
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_current_user(self):
        # URL using path name
        url = reverse('api-accounts:api-auth')

        # Create a user is a workaround in order to authentication works
        user = get_user_model().objects.create_user(username='sahar', email='sahar@mail.com', password='789654',
                                                    full_name='sahar taheri', age='23')
        self.assertEqual(user.is_active, 1, 'Active User')

        # First post to get token
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['token']
        print(token)
        # Next post/get's will require the token to connect
        # self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = self.client.post(reverse('api-accounts:login'), headers={'Authorization':'JWT {0}'.format(token)})
        # response = self.client.post(reverse('api-accounts:login'), format=json)
        print("response", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
# # ................................................................/.
# def test_validate_height(self):
#     factory = APIRequestFactory()
#     request = factory.get('127.0.0.0:8000/bmi')
#     data = {'height': '1.65'}
#     serializer = BmiSerializer(request=request, data=data)
#     serializer.is_valid()
#     self.assertEqual(serializer.validate_height(160), 1.60)
#     self.assertEqual(serializer.validate_height(1.60), 1.60)
# def test_api_jwt(self):
#
#     url = reverse('api-jwt-auth')
#     u = get_user_model().objects.create_user(username='sahar', email='sahar@mail.com', password='789654',
#                                         full_name='sahar taheri', age='23')
#     u.is_active = False
#     u.save()
#
#     resp = self.client.post(url, {'username':'sahar', 'password':'789654'}, format='json')
#     self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
#
#     u.is_active = True
#     u.save()
#
#     resp = self.client.post(url, {'username':'sahar', 'password':'789654'}, format='json')
#     # self.assertEqual(resp.status_code, status.HTTP_200_OK)
#     self.assertFalse('token' in resp.data)
#     token = resp.data['token']

#
# verification_url = reverse('api-jwt-verify')
# resp = self.client.post(verification_url, {'token': token}, format='json')
# self.assertEqual(resp.status_code, status.HTTP_200_OK)
#
# resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
# self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
#
# client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
# resp = client.get('/api/v1/account/', data={'format': 'json'})
# self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
# client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
# resp = client.get('/api/v1/account/', data={'format': 'json'})
# self.assertEqual(resp.status_code, status.HTTP_200_OK)

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
#
#
# class AuthViewsTests(APITestCase):
#
#     def setUp(self):
#         self.username = 'sahar'
#         self.password = '789654'
#         self.data = {
#             'username': self.username,
#             'password': self.password
#         }
#
#     def test_current_user(self):
#         # URL using path name
#         # url = reverse('api-auth-token')
#         url = reverse('api-accounts:login')
#
#         # Create a user is a workaround in order to authentication works
#         user = get_user_model().objects.create_user(username='sahar', email='sahar@mail.com', password='789654',
#                                                     full_name='sahar taheri', age='23')
#         self.assertEqual(user.is_active, 1, 'Active User')
#
#         # First post to get token
#         response = self.client.post(url, self.data, format='json')
#         print(response)
#         self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
#         token = response.data['token']
#
#
#         # Next post/get's will require the token to connect
#         response = self.client.post("api-accounts:login", {}, HTTP_AUTHORIZATION='JWT {}'.format(token))
#         response_content = json.loads(response.content.decode(token))
#         self.assertEqual(response_content["authenticated"], "mooh", "The user should be able to access this endpoint.")
#

# # token = response_content["token"]
# self.client.credentials(HTTP_AUTHORIZATION='Token '+token)
# response = self.client.get(reverse('api-accounts:login'),headers={'Authorization': 'Token ' +token}, data={'format': 'json'})
# print(response)
# self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

# def testDE(self):
#     token = Token.objects.get(user__username='jpmichel')
#     client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
#     response = client.get('/patientFull/1/', headers={'Authorization': 'Token ' + token.key})
#     self.assertEqual(200, response.status_code)
# client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
#
# response = client.patch(self.url_people, serializer.data, format='json')
# self.assertEqual(response.status_code, status.HTTP_200_OK)
# client.logout()

# def test_get_token(self):
#     response = self.client.post("/auth/api/get_token/", {"username": "Heffalumps", "password": "Woozles"})
#     self.assertEqual(response.status_code, 200, "The token should be successfully returned.")
#
#     response_content = json.loads(response.content.decode('utf-8'))
#     token = response_content["token"]
#
#     # The following request fails
#     response = self.client.post("/auth/api/authenticated/", {}, Authorization='JWT ' + token)
#     response_content = json.loads(response.content.decode('utf-8'))
#     self.assertEqual(response_content["authenticated"], "mooh", "The user should be able to access this endpoint.")
