from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import FormParser, MultiPartParser


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
