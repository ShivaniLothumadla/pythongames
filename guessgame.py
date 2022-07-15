import random
lower_boundary = int(input("please enter the lower boundary: "))
upper_boundary = int(input("please enter the upper boundary: "))
num = random.randint(lower_boundary, upper_boundary)
rng = int(input("please enter the range: "))
for i in range(rng):
    guessed_number = int(input("please enter an integer: "))
    if num < guessed_number:
        print('“Try Again! You guessed too high”')
        print(f'you have {rng-i-1} chances remaing')
    elif num > guessed_number:
        print('“Try Again! You guessed too small”')
        print(f'you have {rng-i-1} chances remaing')
    else:
        print(f"you guessed correctly on {i}th time")
        print("congratulations, you won the game")
        break
if i == rng -1:
	print("The actual number is {}".format(num))
	print("Better luck next time")

