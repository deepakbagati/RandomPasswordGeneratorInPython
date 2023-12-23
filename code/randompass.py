import random
import string

def generate_password(length=8):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

random_password = generate_password()
print("Random Password:", random_password)
