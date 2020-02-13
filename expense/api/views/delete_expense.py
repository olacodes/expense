from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.expense import Expense


class DeleteExpense(APIView):
    
    def delete(self, request, user_id, expense_id):
        
        # Get object to be deleted
        expense = get_object_or_404(Expense.objects.all(), id=expense_id)

        # check if user has access to delete the expense
        if expense.user_id.id != user_id:
            return Response({'message': 'You are not allowed to delete this expense'}, status=status.HTTP_400_BAD_REQUEST)
        

        # Delete the expense
        expense.delete()
        return Response({'message': 'expense deleted'}, status=status.HTTP_204_NO_CONTENT)
