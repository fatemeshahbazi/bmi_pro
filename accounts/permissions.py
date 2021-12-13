from rest_framework import permissions
from .models import User

BASE_TOKEN = 'token 35sfdsvsd23#$%#654354fds!fs4'


class SpecificToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is not None and token.casefold() == BASE_TOKEN:
            request.user = User.objects.first()
            return True
        return False
