from rest_framework import generics
from django.contrib.auth.models import User
from .models import Event
from .serializers import EventSerializer, UserSerializer
from rest_framework import generics, permissions


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
