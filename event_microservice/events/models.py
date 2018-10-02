from django.db import models


class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='event', on_delete=models.CASCADE)
    event_name = models.CharField("Nome do Evento", max_length=50)
    linkReference = models.URLField("Link de Referência", max_length=200, default='')
    organizer = models.CharField("Nome para Contato", max_length=50)
    organizerTel = models.CharField("Telefone para Contato", max_length=20, default='')
    value = models.FloatField("Valor do Ingresso", default= '0.0')
    address = models.CharField("Local do Evento", max_length=50)
    linkAddress = models.URLField("Localização no Google Maps", max_length=200, default='')
    eventDate = models.DateField("Data do Rolê", auto_now=False, blank=True)
    eventHour = models.TimeField("Horário do Rolê", auto_now=False, blank=True)
    adultOnly = models.BooleanField("+18", default=False)
    eventDescription = models.TextField("Descrição")
    photo = models.ImageField("Foto", upload_to="media/")
    foods = models.TextField("Comidas")
    drinks = models.TextField("Bebidas")

    class Meta:
        ordering = ('eventDate', 'eventHour', 'event_name',)

    def __str__(self):
        return self.event_name
