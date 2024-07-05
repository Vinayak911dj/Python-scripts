import random

while True:
    print(f'The number is {random.randint(1,6)}')
    user_input=input('Do you want to continue? Y/N:')
    if user_input == 'n':
        break