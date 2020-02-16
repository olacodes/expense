from .helpers import (
    username_regex, password_regex, 
    email_regex, regex_validator, price_regex
)
from rest_framework.response import Response
from rest_framework import status


def check_if_username_exist(table_name, value):
    try:
        query = table_name.objects.get(username=value)
        if query:
            return True
    except:
        return False

def name_validator(name):
    if not name.strip():
        return Response({'message': 'Name field must not be empty'}, status=status.HTTP_400_BAD_REQUEST)
    return True

def username_validator(table_name, username):
    if not username.strip():
        return Response({'message': 'username cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
    if regex_validator(username, username_regex) != True:
        return Response({'message': 'username must bbe minimum of five character without space'}, status=status.HTTP_400_BAD_REQUEST)
    elif check_if_username_exist(table_name, username) ==True:
        return Response({'message': 'username already exist'}, status=status.HTTP_400_BAD_REQUEST)
    return True

def email_validator(email):
    if regex_validator(email, email_regex) !=True:
        return Response({'message': 'Invalid Email'}, status=status.HTTP_400_BAD_REQUEST)
    return True

def password_validator(password):
    if regex_validator(password, password_regex) !=True:
        return Response({'message': 'Password must be minimum five characters, at least one letter and one number'}, status=status.HTTP_400_BAD_REQUEST)
    return True
