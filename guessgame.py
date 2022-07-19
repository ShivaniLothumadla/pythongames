import random
lower_boundary = int(input("please enter the lower boundary: "))
upper_boundary = int(input("please enter the upper boundary: "))
num = random.randrange(lower_boundary, upper_boundary)
rng = int(input("please enter the range: "))
count = 0
for i in range(rng):
    count += 1
    guessed_number = int(input("please enter an integer: "))
    if guessed_number <= 0:
        print("Please enter a positive number next time !!")
        print(f'you have {rng - count} chances remaing')
    elif guessed_number < lower_boundary or guessed_number > upper_boundary:
        print(f'Please enter a number in between {lower_boundary} to {upper_boundary}')
        print(f'you have {rng - count} chances remaing')
    elif num < guessed_number:
        print('“Try Again! You guessed too high”')
        print(f'you have {rng-count} chances remaing')
    elif num > guessed_number:
        print('“Try Again! You guessed too small”')
        print(f'you have {rng-count} chances remaing')
    else:
        print(f"you got it on {count} guesses")
        print("congratulations:), you won the game")
        break
    if count == rng:
        print("The actual number is {}".format(num))
        print("Better luck next time")
