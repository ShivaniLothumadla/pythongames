name = input("type your name: ")
ans = input("Do you want to play adventure game [yes/no]? ").lower().strip()
if ans == 'no':
    print(f"Its an interesting game {name}, wish you could try once")
elif ans == 'yes':
    print(f'Let\'s start the game {name}')
    ans = input("you reach a cross rodes, would you like to go left or right [left/right]? ").lower().strip()
    if ans == 'left':
        ans = input("you encounter a lion, Would you like to run or attack? ").lower().strip()
        if ans == 'run':
            print(f'{name}, Its a good decision, you won the game')
        elif ans == 'attack':
            print(f'{name}, Its not a good choice, you lost the game')
        else:
            print('Invalid choice, you lost')
    elif ans == 'right':
        print("you walk aimlessly to the right and fall on a patch of ice. You injure your leg and cannot move, game over")
    else:
        print('Invalid choice, you lost')
else:
    print("wrong input entered, please type yes/no")
