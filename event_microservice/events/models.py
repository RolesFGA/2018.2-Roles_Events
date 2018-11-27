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
    ownerName = models.CharField(max_length=50, null=True)
    ownerID = models.IntegerField(null=True)
    eventName = models.CharField(max_length=100)
    organizer = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                validators=[not_negative],
                                null=True)
    address = models.TextField()
    latitude = models.FloatField(null=True)
    latitudeDelta = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    longitudeDelta = models.FloatField(null=True)
    eventDate = models.DateField(auto_now=False, validators=[corret_time])
    eventHour = models.TimeField(auto_now=False)
    adultOnly = models.BooleanField(default=False)
    eventDescription = models.TextField(null=True)
    photo = models.URLField()
    foods = models.TextField(null=True)
    drinks = models.TextField(null=True)
    votes = VotableManager()

    class Meta:
        ordering = ('eventDate', 'eventHour', 'eventName',)

    def __str__(self):
        return self.eventName
