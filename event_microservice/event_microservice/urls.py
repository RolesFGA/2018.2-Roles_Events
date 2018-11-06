from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from . import views
from votes import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    url(r'^$', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^', include(urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
