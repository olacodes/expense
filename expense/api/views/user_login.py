from django.contrib.auth import authenticate
import bcrypt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.models import TokenUser

from ..validation.login_validation import LoginValidation
from ..models.user import User
from ..serializers.user_serializer import UserSerializer

class UserLogin(APIView):

    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request,):

        data = request.data
        validate_login = LoginValidation(data)
        validate_empty_fields =  validate_login.check_empty_fields()

        if validate_empty_fields != True:
            return validate_empty_fields
        else:
            validate_user =  validate_login.check_user_exist(User, data['username'].strip())

            if validate_user == False:
                return Response({'message': 'username and password do not match'}, status=status.HTTP_400_BAD_REQUEST)
            else:

                db_username = validate_user.username
                db_password = validate_user.password

                username = data.get('username').strip()
                password = data['password'].strip()

                print(username)
    
                if username != db_username:
                    return Response({'message: username does not exist'}, status=status.HTTP_400_BAD_REQUEST)

                elif not (bcrypt.checkpw(password.encode('utf-8'), db_password.split("'")[1].encode('utf-8'))):
                    return Response({'message: password is incorect'}, status=status.HTTP_400_BAD_REQUEST)
                else:


                    refresh = RefreshToken.for_user(User.objects.get(username=data['username'].strip()))
                    token = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                    return Response({'message': 'success', 'token':token,}, status=status.HTTP_200_OK)
