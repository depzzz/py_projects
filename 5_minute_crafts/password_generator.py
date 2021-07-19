import random

print('Welcome to your Password Generator')

chars = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#?$%^&*()_+=-`,.<>;:[]{}/\|"*-+/.'''

number = int(input("Number of Passwords to Generate: "))
length = int(input("Length of the Passwords: "))

print("Here are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)