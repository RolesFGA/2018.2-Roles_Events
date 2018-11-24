from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
