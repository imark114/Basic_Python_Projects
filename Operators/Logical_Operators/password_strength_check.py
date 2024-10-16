# Password Strength Checker: Assess the strength of a password based on various criteria like length, character types, and using logical operators to combine requirements.

import string
def check_password_strength(password):
    pass_len = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char not in string.ascii_letters + string.digits for char in password)

    if pass_len < 8:
        strength = "Weak"
    elif (has_uppercase and has_lowercase and has_digit and has_special_char):
        strength = "Strong"
    elif (has_uppercase or has_lowercase) and (has_digit or has_special_char):
        strength = "Medium"
    else:
       strength =  "Weak"
    return strength

password = input("Enter Your Password: ")
strength = check_password_strength(password)
print(f"Password Strength {strength}")