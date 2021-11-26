from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth-token/', obtain_jwt_token),
    path('api-auth-refresh/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('bmi/', include('core.urls', namespace='core'))
]
