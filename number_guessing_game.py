import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

top_of_range = input("Please enter the top range: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if int(top_of_range) <= 0:
        print('Please enter the number greater than 0 next time ')
        quit()
else:
    print('Please enter only the digit ')
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_choice = input('Make a guess :')
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice > top_of_range:
            print(f'Please enter a number upto {top_of_range}')
    else:
        print('Please enter only the digit next time ')

    if user_choice == random_number:
        print(f'{Fore.CYAN + Back.WHITE + Style.BRIGHT}You guessed correctly:) : The number is {random_number}')
        break
    elif user_choice < random_number:
        print(f'you were guessed too low ')
    else:
        print(f'you were guessed too high ')

print(f'You got in {guesses} guesses')