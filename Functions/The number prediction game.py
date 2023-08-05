import random
import time

print("""
************************************
NUMBER GUESSING GAME

Guess the number between 1 and 40
************************************
""")

MIN_NUMBER = 1
MAX_NUMBER = 40
MAX_GUESS_COUNT = 7

random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
remaining_guesses = MAX_GUESS_COUNT

while remaining_guesses > 0:
    guess = int(input("Your guess: "))

    if guess < random_number:
        time.sleep(1)
        print("Enter a higher number.")
    elif guess > random_number:
        time.sleep(0.5)
        print("Enter a lower number.")
    else:
        time.sleep(1)
        print("Congratulations, you guessed correctly!")
        break

    remaining_guesses -= 1

if remaining_guesses == 0:
    print("Out of guesses....")
    print("The number was:", random_number)
