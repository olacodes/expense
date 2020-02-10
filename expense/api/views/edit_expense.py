from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..serializers.expense_serializer import ExpenseSerializer
from ..serializers.user_serializer import UserSerializer
from ..models.expense import Expense
from ..models.user import User

# How do i populate the data to the form
class EditExpense(APIView):
    serializer_class = ExpenseSerializer

    def put(self, request, user_id, expense_id, format=None):
        # Get saved expense
        expense_object = Expense.objects.get(id=expense_id)
        print(expense_object.value)
        
        # Get the modified expense
        data = request.data
        print(data)
        # serialize the modified expens
        serializer = ExpenseSerializer(instance=expense_object, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Expense successfully updated'}, status=status.HTTP_200_OK)
        return Response({'message':'Error'}, status=status.HTTP_400_BAD_REQUEST)
