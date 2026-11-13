# projec1 - Nubmer guessing game

import random

print('Number Guessing Game')

random_number = random.randint(1,100)

guessed_number = 0

number_of_guess = 0

while guessed_number != random_number:
    try:
      guessed_number = int(input('Guess the number : '))
    except ValueError:
         print('Enter a value between 1 to 100')
         continue
    number_of_guess += 1

    if guessed_number > 100:
         print('Number > 100 is not allowed')
    elif guessed_number > random_number:
         print('Too high!')
    elif guessed_number < random_number:
         print('Too low!')
    else:
        print('Congratulations! You guessed it!')

    
print(f'number of guess : {number_of_guess}')


