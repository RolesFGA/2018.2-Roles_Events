from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from votes.managers import VotableManager


def not_negative(value):
    if value < 0:
        raise ValidationError('Numero não pode ser negativo')


def corret_time(value):
    today = date.today()
    if value < today:
        raise ValidationError('Tempo incorreto')


class Event(models.Model):
    ownerName = models.CharField(max_length=50, default="")
    ownerID = models.IntegerField(default=0)
    eventName = models.CharField(max_length=100)
    linkReference = models.URLField(max_length=200, default="")
    organizer = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                validators=[not_negative],
                                default=0.00)
    address = models.TextField()
    latitude = models.IntegerField(default=0)
    latitudeDelta = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    longitudeDelta = models.IntegerField(default=0)
    eventDate = models.DateField(auto_now=False, validators=[corret_time])
    eventHour = models.TimeField(auto_now=False)
    adultOnly = models.BooleanField(default=False)
    eventDescription = models.TextField(default="")
    photo = models.URLField()
    foods = models.TextField(default="")
    drinks = models.TextField(default="")
    votes = VotableManager()

    class Meta:
        ordering = ('eventDate', 'eventHour', 'eventName',)

    def __str__(self):
        return self.eventName
