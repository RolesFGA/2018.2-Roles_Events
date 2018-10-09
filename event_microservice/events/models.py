from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def not_negative(value):
    if value < 0:
        raise ValidationError('Numero não pode ser negativo')

def corret_time(value):
    today = date.today()
    if value < today:
        raise ValidationError('Tempo incorreto')


class Event(models.Model):
    owner = models.CharField("Criador do Evento", max_length=50, default="")
    eventName = models.CharField("Nome do Evento", max_length=50)
    linkReference = models.URLField("Link de Referência", max_length=200, default="")
    organizer = models.CharField("Nome para Contato", max_length=50)
    value = models.DecimalField("Valor do Ingresso", max_digits=12, decimal_places=2, validators=[not_negative], default=0.00)
    address = models.CharField("Local do Evento", max_length=50)
    linkAddress = models.URLField("Localização no Google Maps", max_length=200, default="")
    eventDate = models.DateField("Data do Rolê", auto_now=False, help_text="DD/MM/AAAA", validators=[corret_time])
    eventHour = models.TimeField("Horário do Rolê", auto_now=False)
    adultOnly = models.BooleanField("+18", default=False, help_text="Marque caso seja só para adultos")
    eventDescription = models.TextField("Descrição", help_text="Descrição do evento")
    photo = models.ImageField("Foto", default="")
    foods = models.TextField("Comidas")
    drinks = models.TextField("Bebidas")

    class Meta:
        ordering = ('eventDate', 'eventHour', 'eventName',)

    def __str__(self):
        return self.eventName
