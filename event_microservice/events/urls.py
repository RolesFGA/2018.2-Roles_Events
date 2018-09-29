from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
