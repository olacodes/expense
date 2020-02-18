from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.user import User
from ..models.expense import Expense
from ..serializers.expense_serializer import ExpenseSerializer

from ..validation.expense_validation import ExpenseValidator

class NewExpense(APIView):

    serializer_class = ExpenseSerializer

    def post(self, request, user_id):

        data = request.data
        
        validate_value = ExpenseValidator.validate_price(data['value'])
        validate_reason = ExpenseValidator.validate_reason(data['reason'])

        if validate_value != True:
            return validate_value

        if validate_reason != True:
            return validate_reason
            
        # get the user_id from the User object
        user_id = get_object_or_404(User.objects.all(), id=user_id)

        expense = Expense.objects.create(
            value = data['value'],
            reason = data['reason'].capitalize(),
            user_id = user_id
        )

        expense.save()
        return Response({'message': 'expense successfully create'}, status=status.HTTP_201_CREATED)
