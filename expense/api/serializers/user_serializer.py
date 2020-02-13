# from rest_framework.authtoken.models import Token
from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    
    confirm_password = {'password': {'write_only': True}}
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

        # overide the save method to confirm the password
        def create(self, validated_data):
            user = User(
                username = self.validated_data['username'],
                email = self.validated_data['email']
            )
            password = self.validated_data['password']
            confirm_password = self.validated_data['confirm_password']

            if confirm_password != password:
                raise serializers.ValidationError({'password': 'password must match' })

            user.set_password(password)

            user.save()
            # Token.objects.create(user=user)
            return user
            