import re
# must be a valid email address
email_regex =  "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# Minimum five characters, at least one letter and one number:
password_regex = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d._@#$%^&(!)]{5,}$'

# Minimum of five characters and must be unique
username_regex = '[A-Za-z\d._@#$%^&(!)]{5,}$'

price_regex = '^([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9][0-9])?$'

def regex_validator(value, regex):
    if not value:
        return False
    else:
        return bool(re.search(regex, value))
