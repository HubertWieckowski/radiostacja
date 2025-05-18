from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artist, Hit

class HitAPITest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(first_name="Test", last_name="Artist")
        self.hit = Hit.objects.create(title="Test Hit", artist=self.artist)

    def test_get_hit_list(self):
        url = reverse('hit-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_hit(self):
        url = reverse('hit-list-create')
        data = {'title': 'New Hit', 'artist': self.artist.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
