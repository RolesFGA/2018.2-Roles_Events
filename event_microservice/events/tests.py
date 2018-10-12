from django.test import TestCase
from .models import Event


class ModelTestCase(TestCase):
    """This class defines the test suite for the event model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.eventName = "Teste"
        self.eventDate = "2018-05-05"
        self.eventHour = "03:03:00"
        self.organizer = "Henrique"
        self.address = "Here"
        self.eventDescription = "Chato"
        self.foods = "Comidas"
        self.drinks = "Bebidas"

        self.event = Event (eventName=self.eventName,
                            eventDate=self.eventDate,
                            eventHour=self.eventHour,
                            organizer=self.organizer,
                            address=self.address,
                            eventDescription=self.eventDescription,
                            foods=self.foods,
                            drinks=self.drinks)

    def test_model_can_create_a_event(self):
        """Test the bucketlist model can create a event."""
        
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)
