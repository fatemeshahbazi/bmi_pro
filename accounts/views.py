from django.shortcuts import render
from .serializers import UserLoginSerializer, UserRegisterSerializer
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response
import jwt
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserRegisterApiView(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = JSONWebTokenAuthentication,

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = JSONWebTokenAuthentication,

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            print(settings.JWT_SECRET_KEY)
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")
            serializer = UserLoginSerializer(user)
            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogOutAPIView(APIView):
    authentication_classes = JSONWebTokenAuthentication,
    permission_classes = [AllowAny, ]

    def get(self, request):
        user = getattr(request, 'user', None)
        if not getattr(user, 'is_authenticated', True):
            user = None
        request.session.flush()
        if hasattr(request, 'user'):
            from django.contrib.auth.models import AnonymousUser
            request.user = AnonymousUser()
        return Response()