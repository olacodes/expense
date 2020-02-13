from .validation import password_validator, email_validator, name_validator, username_validator


def user_validation(table_name, data):
    validate_name = name_validator(data.get('name', ''))
    validat_username = username_validator(table_name, data.get('username', '')) 
    validate_email = email_validator(data.get('email', ''))
    validate_password = password_validator(data.get('password', '')) 
    
    if validate_name != True:
        return validate_name
    elif validat_username != True:
        return validat_username
    elif  validate_email != True:
        return validate_email
    elif validate_password != True:
        return validate_password
    return True
