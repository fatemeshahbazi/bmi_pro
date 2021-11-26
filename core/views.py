from rest_framework.response import Response
from accounts.models import User
from .serializers import BmiSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import BmiMeasurement


class BmiCreate(APIView):
    serializer_class = BmiSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = JSONWebTokenAuthentication,

    @classmethod
    def get_serializer(cls):
        return cls.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer()(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated:
            serializer.save(user=request.user)
        else:
            serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        if request.user.is_anonymous:
            return Response({'message': 'You must login first'}, status=401)
        user = request.user
        queryset = BmiMeasurement.objects.filter(user=user)
        return Response(serializer(queryset, many=True).data, status=200)
