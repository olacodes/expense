from django.urls import path, include
from .views import (
    user_login,
    user_registration,
    expense,
    new_expense,
    edit_expense,
    delete_expense
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', user_registration.UserRegistration.as_view(), name='user_registration'),
    path('login/', user_login.UserLogin.as_view(), name='user_login' ),
    path('<int:user_id>/expense/', expense.UserExpense.as_view(), name='expense_list'),
    path('<int:user_id>/expense/new/', new_expense.NewExpense.as_view(), name='new_expense'),
    path('<int:user_id>/expense/<int:expense_id>/edit/', edit_expense.EditExpense.as_view(), name='edit_expense'),
    path('<int:user_id>/expense/<int:expense_id>/delete/', delete_expense.DeleteExpense.as_view(), name='delete_expense')

]
