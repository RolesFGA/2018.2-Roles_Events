from django.db import models

class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='event', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    linkReference = models.URLField(max_length=200, default='')
    organizer = models.CharField(max_length=50)
    organizerTel = models.CharField(max_length=20, default='')
    value = models.FloatField(default= '0.0')
    address = models.CharField(max_length=50)
    linkAddress = models.URLField(max_length=200, default='')
    eventDate = models.DateField(auto_now=False, blank=True)
    eventHour = models.TimeField(auto_now=False, blank=True)
    adultOnly = models.BooleanField(default=False)
    eventDescription = models.TextField()
    photo = models.ImageField()
    foods = models.TextField()
    drinks = models.TextField()

    class Meta:
        ordering = ('eventDate', 'eventHour', 'event_name',)

    def __str__(self):
        return self.event_name
