import re

def validate_pattern(pattern, text):
    if re.match(pattern, text):
        return True
    else:
        return False

# Validate an email address
def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return validate_pattern(email_pattern, email)

# Validate a Bangladeshi mobile number
def validate_bangladesh_mobile(mobile):
    mobile_pattern = r'^01[3-9]\d{8}$'
    return validate_pattern(mobile_pattern, mobile)

# Validate a USA telephone number (assuming standard format with or without hyphens)
def validate_usa_telephone(telephone):
    telephone_pattern = r'^\d{3}-?\d{3}-?\d{4}$'
    return validate_pattern(telephone_pattern, telephone)

# Validate a 16-character alphanumeric password with uppercase, lowercase, special characters, and numbers
def validate_password(password):
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=\S+$).{16}$'
    return validate_pattern(password_pattern, password)

# Test the validation functions
email = "example@email.com"
mobile = "01987654321"
telephone = "123-456-7890"
password = "Abcd1234@5678xyz"

print(f"Email is valid: {validate_email(email)}")
print(f"Mobile number is valid: {validate_bangladesh_mobile(mobile)}")
print(f"Telephone number is valid: {validate_usa_telephone(telephone)}")
print(f"Password is valid: {validate_password(password)}")