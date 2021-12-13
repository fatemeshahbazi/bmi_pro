from django.urls import path
from .views import UserRegisterApiView, UserLoginView, LogOutAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


app_name = 'api-accounts'
urlpatterns = [
    path('register/', UserRegisterApiView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutAPIView.as_view(), name='logout'),
    path('api-auth-token/', obtain_jwt_token, name='api-auth'),
    path('api-auth-refresh/', refresh_jwt_token),
]
