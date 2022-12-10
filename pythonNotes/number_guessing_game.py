# date: 18.08.22,  @author...

# number guessing game
import random

number = random.randint(1, 10)

player_name = input("Hello, What's your name? ")
print('okay! ' + player_name + ' I am Guessing a number between 1 an 10: ')

# set a value 0, to number_of_guesses
number_of_guesses = 0

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print("your guess is too low")
    if guess > number:
        print("your guess is too high")
    if guess == number:
        break


if guess == number:
    print("You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("You did not guess the number, The number was " + str(number))