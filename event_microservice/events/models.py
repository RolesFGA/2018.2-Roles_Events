from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    organizer = models.CharField(max_length=50)
    value = models.FloatField(default= '0.0')
    amount = models.IntegerField(default= '0')
    address = models.TextField()
    foods = models.TextField()
    drinks = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.event_name
