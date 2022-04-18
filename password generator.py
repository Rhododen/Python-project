import string
import random

print('''Hi there!
Welcome to the password generator''')


alphabet = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
characters = list(alphabet + numbers + symbols)

def generate_password():
    password_length = int(input('\nEnter the length of password: '))

    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    generated_password = ''.join([str(item) for item in password])
    print(generated_password)

generate_password()

