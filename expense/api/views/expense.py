from rest_framework.views import APIView
from ..models.expense import Expense
from ..models.user import User
from rest_framework.response import Response

from ..serializers.expense_serializer import ExpenseSerializer

class UserExpense(APIView):
    
    def get(self, response, user_id):
        user = User.objects.get(id=user_id)
        user_expenses = Expense.objects.filter(user_id=user.id)
        serializer = ExpenseSerializer(user_expenses, many=True)
        return Response(serializer.data)
        
