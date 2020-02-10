from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .mock_data import MockData


class TestUser(APITestCase):
    client = APIClient()
    def test_user_registration(self):
        url = reverse('user_registration')
        response = self.client.post(url, MockData.user_data(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        MockData.setup()
        url = reverse('user_login')
        response = self.client.post(url, MockData.user_data(), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

