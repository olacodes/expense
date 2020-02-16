from rest_framework.response import Response
from rest_framework import status
 
class LoginValidation:
    def __init__(self, data):
        self.data = data

    def check_empty_fields(self):
        if self.data.get('username').strip() == None:
            return Response({'message: Username cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        elif self.data.get('password').strip() == None:
            return Response({'message: password cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return True
    
    def check_user_exist(self, model, username):
        try:
            query = model.objects.get(username=username)
            return query
        except:
            return False

    