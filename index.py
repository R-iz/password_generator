import random
import string


def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation


    # Generate a password of specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password


# Get desired password length from the user
try:
    length = int(input("Enter the desired length of the password: "))
    if length < 4:
        print("Password length should be at least 4 characters for complexity.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for the password length.")
