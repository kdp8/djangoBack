from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Actor
from django.utils import timezone

class TopActorsAPITest(TestCase):
    def setUp(self):
        self.actor1 = Actor.objects.create(first_name='John', last_name='Doe', last_update=timezone.now())
        self.actor2 = Actor.objects.create(first_name='Jane', last_name='Smith', last_update=timezone.now())
        self.actor3 = Actor.objects.create(first_name='Alice', last_name='Johnson', last_update=timezone.now())

    def test_top_actors_api(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/top-actors/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        self.assertEqual(response.data[0]['first_name'], 'John')
        self.assertEqual(response.data[0]['last_name'], 'Doe')
        self.assertEqual(response.data[0]['film_count'], 0)
        
        self.assertEqual(response.data[1]['first_name'], 'Jane')
        self.assertEqual(response.data[1]['last_name'], 'Smith')
        self.assertEqual(response.data[1]['film_count'], 0)

        self.assertEqual(response.data[2]['first_name'], 'Alice')
        self.assertEqual(response.data[2]['last_name'], 'Johnson')
        self.assertEqual(response.data[2]['film_count'], 0)

  