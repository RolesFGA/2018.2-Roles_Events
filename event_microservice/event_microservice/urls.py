from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('events.urls')),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
]
