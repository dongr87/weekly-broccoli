"""
Utilize Python's random module to generate random characters and string module to get character sets for passwords.
"""
import random
import string

def generate_pwd(length: int = 8):
    """
    input:
        digits: length of the password to be generated, default to 8
    """
    characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

password = generate_pwd(20)
print("Generated Password:", password)