from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models.expense import Expense
from ..models.user import User
from ..serializers.expense_serializer import ExpenseSerializer

class UserExpense(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, response, user_id):
        user = get_object_or_404(User.objects.all(), id=user_id)
        user_expenses = Expense.objects.filter(user_id=user.id)
        serializer = ExpenseSerializer(user_expenses, many=True)
        return Response(serializer.data)
        
