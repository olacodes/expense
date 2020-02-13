from ..models.user import User
from ..models.expense import Expense
import bcrypt

class MockData:
    @classmethod
    def user_data(cls):
        return {
            'id': 1,
            'name': 'olatunde',
            'username': 'sodiq',
            'email': 'olatundesodiq@gmail.com',
            'password': 'olatunde123'
        }
    @classmethod
    def create_user(cls):
        data = MockData.user_data()
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        user = User(
            id = data['id'],
            name = data['name'],
            username = data['username'],
            email = data['email'],
            password = hashed,
        )
        user.save()
        return user

    @classmethod
    def expense_data(cls):
        return {
            'user_id': 1,
            'value': '2000',
            'reason': 'Testin testing'
        }
    @classmethod
    def create_user_expense(cls):
        hashed = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())

        user = User(
            name = 'name',
            username = 'username',
            email = 'email',
            password = hashed,
        )
        user.save()
        return user


    @classmethod
    def create_expense(cls):
        data = MockData.expense_data()
        user = MockData.create_user_expense()
        expense = Expense(
            user_id = user,
            value = data['value'],
            reason = data['reason']
        )



