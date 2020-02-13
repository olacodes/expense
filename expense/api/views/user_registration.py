import bcrypt

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.models import TokenUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.user import User
from ..validation.user_validation import user_validation
from ..serializers.user_serializer import UserSerializer

class UserRegistration(APIView):

    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()
    
    def post(self, request):
        data = request.data
        validate_user = user_validation(User, data)
        if validate_user != True:
            return validate_user
        else:
            hashed = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt()
                )
            user = User.objects.create(
                name = data['name'],
                username = data['username'],
                password = hashed,
                email = data['email']
            )
            # save user to database
            user.save()
            refresh = RefreshToken.for_user(User.objects.get(username=data['username']))
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response({'message': 'user successfully created', 'token':token} , status=status.HTTP_201_CREATED)
