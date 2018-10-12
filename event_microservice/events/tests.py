from django.test import TestCase
from .models import Event
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse, resolve


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

        self.event = Event (eventName=self.eventName, eventDate=self.eventDate,eventHour=self.eventHour,organizer=self.organizer,address=self.address,eventDescription=self.eventDescription,foods=self.foods,drinks=self.drinks)

    def test_model_can_create_a_event(self):
        """Test the event model can create a event."""
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.event_data = {'eventName': 'Teste1',
                           'eventDate': "2018-12-12",
                           'eventHour': "03:03:00",
                           'organizer': "Henrique",
                           'address': "Here",
                           'eventDescription': "Chato",
                           'foods': "Comidas",
                           'drinks': "Bebidas"}
        self.response1 = self.client.post(
            reverse('event-list'),
            self.event_data,
            format="json")

        self.event_data2 = {'eventName': 'Teste2',
                           'eventDate': "2018-05-05",
                           'eventHour': "03:03:00",
                           'organizer': "Henrique",
                           'address': "Here",
                           'eventDescription': "Chato",
                           'foods': "Comidas",
                           'drinks': "Bebidas"}
        self.response2 = self.client.post(
            reverse('event-list'),
            self.event_data2,
            format="json")

    """ Test: Creating """

    def test_api_event_create(self):
        """Test the api has event creation capability."""
        self.assertEqual(self.response1.status_code, status.HTTP_201_CREATED)

    """ Test: Getting """

    def test_api_event_get(self):
        """Test the api can get a given event."""
        event = Event.objects.get()
        response = self.client.get(
            reverse('event-detail',
            kwargs={'pk': event.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)

    """ Test: Updating """

    def test_api_event_update(self):
        """Test the api can update a given event."""
        event = Event.objects.get()
        change_event1 = {'eventName': 'Mudei este campo',
                        'eventDate': "2018-12-12",
                        'eventHour': "03:03:00",
                        'organizer': "Henrique",
                        'address': "Here",
                        'eventDescription': "Chato",
                        'foods': "Comidas",
                        'drinks': "Bebidas"}
        res = self.client.put(
            reverse('event-detail',
            kwargs={'pk': event.id}), change_event1, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        """ Test the api cannot update if date is incorret """

        change_event2 = {'eventName': 'Teste',
                        'eventDate': "2018-05-05",
                        'eventHour': "03:03:00",
                        'organizer': "Henrique",
                        'address': "Here",
                        'eventDescription': "Chato",
                        'foods': "Comidas",
                        'drinks': "Bebidas"}
        res2 = self.client.put(
            reverse('event-detail',
            kwargs={'pk': event.id}), change_event2, format='json'
        )
        self.assertEqual(res2.status_code, status.HTTP_400_BAD_REQUEST)

        """ Test the api cannot update if value is negative """

        change_event3 = {'eventName': 'Teste',
                        'eventDate': "2018-05-05",
                        'eventHour': "03:03:00",
                        'organizer': "Henrique",
                        'value': -2,
                        'address': "Here",
                        'eventDescription': "Chato",
                        'foods': "Comidas",
                        'drinks': "Bebidas"}
        res3 = self.client.put(
            reverse('event-detail',
            kwargs={'pk': event.id}), change_event3, format='json'
        )
        self.assertEqual(res3.status_code, status.HTTP_400_BAD_REQUEST)
