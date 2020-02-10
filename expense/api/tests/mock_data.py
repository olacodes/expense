from ..models.user import User
import bcrypt

class MockData:
    @classmethod
    def user_data(cls):
        return {
            'name': 'olatunde',
            'username': 'sodiq',
            'email': 'olatundesodiq@gmail.com',
            'password': 'olatunde123'
        }
    @classmethod
    def setup(cls):
        data = MockData.user_data()
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(
            name = data['name'],
            username = data['username'],
            email = data['email'],
            password = hashed,
        )
        user.save()
