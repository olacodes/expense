from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.expense_serializer import ExpenseSerializer
from ..serializers.user_serializer import UserSerializer
from ..models.expense import Expense
from ..models.user import User
from ..validation.expense_validation import ExpenseValidator

class EditExpense(APIView):
    serializer_class = ExpenseSerializer

    def put(self, request, user_id, expense_id, format=None):

        # Get saved expense
        expense_object = get_object_or_404(Expense, id=expense_id)

        # check if user have access to edit the expense
        if expense_object.user_id.id != user_id:
            return Response({'User Error': 'You do not have access to edit this expense'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the modified expense
        data = request.data

        # validate the modified expense value
        validate_value = ExpenseValidator.validate_price(data['value'])
        if validate_value != True:
            return validate_value

        # validate modified reason 
        validate_reason = ExpenseValidator.validate_reason(data['reason'])
        if validate_reason != True:
            return validate_reason

        # serialize the modified expens
        serializer = ExpenseSerializer(instance=expense_object, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Expense successfully updated'}, status=status.HTTP_200_OK)
        return Response({'message':'Error'}, status=status.HTTP_400_BAD_REQUEST)
