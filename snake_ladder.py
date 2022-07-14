import random
snake_dict = {98: 6, 95: 44, 92: 78, 83: 57, 77: 62, 55: 4, 44: 12, 34: 1}
ladder_dict = {6: 23, 29: 48, 54: 75, 33: 47, 56: 70, 67: 72, 79: 88, 82: 99}
player1_name = input("please enter player1 name: ")
player2_name = input("please enter player2 name: ")
player1_value = player2_value = player_value = 0
player_id = 1
player1_id = 1
player2_id = 2
while player1_value <= 100 or player2_value <= 100:
    temp1, temp2 = player1_value, player2_value
    if player1_value == 100 or player2_value == 100:
        if player1_value == 100:
            print(f'\nCongratulations {player1_name}, you won the game:)')
            break
        else:
            print(f'\nCongratulations {player2_name}, you won the game:)')
            break
    if player_id == player1_id:
        print(f"{player1_name}, please roll the dice")
        player_name = player1_name
        player_value = player1_value
    else:
        print(f"{player2_name}, please roll the dice")
        player_name = player2_name
        player_value = player2_value
    input("press enter !!!")
    dice = random.randint(1, 6)
    print(f"\n{player_name}, you got {dice}")
    if player_value + dice <= 100:
        player_value += dice
    else:
        print(f'{player_name}, you just need {100 - player_value}')
        print(f'{player_name}, you are now at {player_value}')
        if player_id == player1_id:
            player1_value = player_value
            player_id = player2_id

        else:
            player_id = player1_id
            player2_value = player_value

    print(f'{player_name}, you are now at {player_value}')
    if player_value in snake_dict:
        print(f'{player_name}, you caught by snake at {player_value}')
        player_value = snake_dict[player_value]
        print(f'{player_name}, you are now at {player_value}')
    elif player_value in ladder_dict:
        print(f'{player_name}, you got ladder at {player_value}')
        player_value = ladder_dict[player_value]
        print(f'{player_name}, you are now at {player_value}')
    if dice != 6:
        if player_id == player1_id:
            player1_value = player_value
            player_id = player2_id

        else:
            player_id = player1_id
            player2_value = player_value

    else:
        print(f"{player_name}, please roll the dice again because you got 6 earlier.")
        input("press enter !!!")
        dice = random.randint(1, 6)
        print(f"\n{player_name}, you got {dice}")
        if player_value + dice <= 100:
            player_value += dice
        else:
            print(f'{player_name}, you just need {100 - player_value}')
            print(f'{player_name}, you are now at {player_value}')
            if player_id == player1_id:
                player1_value = player_value
                player_id = player2_id

            else:
                player_id = player1_id
                player2_value = player_value

        print(f'{player_name}, you are now at {player_value}')
        if player_value in snake_dict:
            print(f'{player_name}, you caught by snake at {player_value}')
            player_value = snake_dict[player_value]
            print(f'{player_name}, you are now at {player_value}')
        elif player_value in ladder_dict:
            print(f'{player_name}, you got ladder at {player_value}')
            player_value = ladder_dict[player_value]
            print(f'{player_name}, you are now at {player_value}')
        if dice != 6:
            if player_id == player1_id:
                player1_value = player_value
                player_id = player2_id

            else:
                player_id = player1_id
                player2_value = player_value

        else:
            print(f"{player_name}, please roll the dice again because you already got 6 two times continuously")
            input("press enter !!!")
            dice = random.randint(1, 6)
            print(f"\n{player_name}, you got {dice}")
            if player_value + dice <= 100:
                player_value += dice
            else:
                print(f'{player_name}, you just need {100 - player_value}')
                print(f'{player_name}, you are now at {player_value}')
                if player_id == player1_id:
                    player1_value = player_value
                    player_id = player2_id

                else:
                    player_id = player1_id
                    player2_value = player_value

            print(f'{player_name}, you are now at {player_value}')
            if player_value in snake_dict:
                print(f'{player_name}, you caught by snake at {player_value}')
                player_value = snake_dict[player_value]
                print(f'{player_name}, you are now at {player_value}')
            elif player_value in ladder_dict:
                print(f'{player_name}, you got ladder at {player_value}')
                player_value = ladder_dict[player_value]
                print(f'{player_name}, you are now at {player_value}')
            if dice != 6:
                if player_id == player1_id:
                    player1_value = player_value
                    player_id = player2_id

                else:
                    player_id = player1_id
                    player2_value = player_value

            else:
                if player_name == player1_name:
                    print(f'{player_name} you are supposed to be at {player_value},'
                          f' as you got 6 three times continuously, so you have to start from previous position {temp1}')
                    player1_value = temp1
                    player_id = player2_id

                else:
                    print(f'{player_name} you are supposed to be at {player_value},'
                          f' as you got 6 three times continuously, so you have to start from previous position {temp2}')
                    player1_value = temp2
                    player_id = player1_id

