from django.db import models


class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='event', on_delete=models.CASCADE)
    event_name = models.CharField("Nome do Evento", max_length=50)
    linkReference = models.URLField("Link de Referência", max_length=200, help_text="Com quem entrar em contato caso necessário")
    organizer = models.CharField("Nome para Contato", max_length=50)
    organizerTel = models.CharField("Telefone para Contato", max_length=20, help_text="Ex: (61) 91234-5678")
    value = models.FloatField("Valor do Ingresso", help_text="Ex: 49,99")
    address = models.CharField("Local do Evento", max_length=50)
    linkAddress = models.URLField("Localização no Google Maps", max_length=200)
    eventDate = models.DateField("Data do Rolê", auto_now=False, help_text="DD/MM/AAAA")
    eventHour = models.TimeField("Horário do Rolê", auto_now=False)
    adultOnly = models.BooleanField("+18", default=False, help_text="Marque caso seja só para adultos")
    eventDescription = models.TextField("Descrição", help_text="Descrição do evento")
    photo = models.ImageField("Foto")
    foods = models.TextField("Comidas", help_text="Lista de comidas do evento")
    drinks = models.TextField("Bebidas", help_text="Lista de bebidas do evento")

    class Meta:
        ordering = ('eventDate', 'eventHour', 'event_name',)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        self.value = round(self.value, 2)
        super(Event, self).save(*args, **kwargs)
