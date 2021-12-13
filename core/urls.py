from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import BmiCreate

app_name = 'core'

urlpatterns = [
    path('', BmiCreate.as_view(), name="bmicreate"),

]
