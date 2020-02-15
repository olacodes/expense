from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.models import TokenUser
from .mock_data import MockData


class TestExpense(APITestCase):
    
    client = APIClient()

    def test_get_all_expense(self):
        user = MockData.create_user()
        self.client.force_authenticate(TokenUser)
        response = self.client.get(f'/api/{user.id}/expense/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_expense(self):
        expense = MockData.create_expense()
        response = self.client.put(
            f'/api/{expense.user_id.id}/expense/{expense.id}/edit/', 
            MockData.update_data(),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_expense(self):
        expense = MockData.create_expense()
        response = self.client.delete(
            f'/api/{expense.user_id.id}/expense/{expense.id}/delete/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_expense(self):
        user = MockData.create_user()
        response = self.client.post(
            f'/api/{user.id}/expense/new/',
            MockData.expense_data()
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

