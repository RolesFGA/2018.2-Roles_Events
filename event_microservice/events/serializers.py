from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Event
        fields = '__all__'
