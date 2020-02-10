from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.expense import Expense


class DeleteExpense(APIView):

    def delete(self, request, user_id, expense_id):
        expense = get_object_or_404(Expense.objects.all(), id=expense_id)
        expense.delete()
        return Response({'message': 'expense deleted'}, status=status.HTTP_204_NO_CONTENT)
