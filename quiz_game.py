print("Welcome to the Quiz game! ")
playing = input("\nDo you want to play?y/n/yes/no ")
if playing.lower() not in ['y', 'yes']:
    quit()
print('\nOkay, Let\'s continue')
score = 0
answer = input("what does CPU stands for? ")
if answer.lower() == 'central processing unit':
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
answer = input("what does GPU stands for? ")
if answer.lower() == 'graphics processing unit':
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')

answer = input("what does RAM stands for? ")
if answer.lower() == 'random access memory':
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')

answer = input("what does PSU stands for? ")
if answer.lower() == 'power supply unit':
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
print(f'You got {score} questions correct!')
print(f'You got {(score/4) * 100} %.')
