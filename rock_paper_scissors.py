"""
2 players --computer and player
a list ['rock', 'paper', 'scissors']
a random number by using randint or randerange
rock crushes scissors
paper covers rock
scissors cut paper
"""
import random
options = ['rock', 'paper', 'scissors']
user_wins = computer_wins = 0
while True:
    user_input = input('type rock/paper/scissors/r/p/s or q to quit the game! ').lower()
    if user_input == 'q':
        break
    if user_input not in options and user_input not in ['r', 'p', 's']:
        continue
    random_number = random.randint(0, 2)
    computer_picked = options[random_number]
    print(f'computer picked {computer_picked}')
    if user_input in ['rock', 'r'] and computer_picked in ['scissors', 's']:
        print('you win:)')
        user_wins += 1
    elif user_input in ['paper', 'p'] and computer_picked in ['rock', 'r']:
        print('you win!:)')
        user_wins += 1
    elif user_input in ['scissors', 's'] and computer_picked in ['paper', 'p']:
        print('you win!:)')
        user_wins += 1
    elif user_input == computer_picked:
        print('Draw!!')
    else:
        print('you lost:(')
        computer_wins += 1
print(f'you won {user_wins} times.')
print(f'computer won {computer_wins} times.')