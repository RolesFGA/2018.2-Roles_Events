from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    url(r'^$', views.api_root),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
