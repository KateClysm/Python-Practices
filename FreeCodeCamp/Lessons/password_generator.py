import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    letters = string.ascii_letters # Define the possible characters for the password
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols # Combine all characters

    while True:
        password = ''
        
        for _ in range(length): # Generate password
            password += secrets.choice(all_characters)
        
        constraints = [ #restricciones
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        if all(   # Check constraints   
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)