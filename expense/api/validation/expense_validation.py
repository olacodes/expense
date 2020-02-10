from rest_framework.response import Response
from .helpers import regex_validator, price_regex

class ExpenseValidator:
    
    # validate the price is in right format
    def validate_price(self, price):
        if not price.strip():
            return Response({'message': 'value must not be empty'}, status=status.HTTP_400_BAD_REQUEST)
        elif regex_validator(price, price_regex) == False:
            return Response({'message': 'Enter a valid amount'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return True
        
