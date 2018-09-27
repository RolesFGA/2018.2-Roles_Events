from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from events.models import Event

class TestEvent(TestCase):
    def setUp(self):
        self.event = mommy.make(Event, event_name = 'evento teste')

    def test_event_creation(self):
      self.assertTrue(isinstance(self.event, Event))
      self.assertEquals(self.event.__str__(), self.event.event_name)
