import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 99.")
attempts = 0
answer = random.randint(0, 99)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"Correct! The answer was {answer}. You win!")
        break
    elif guess < answer:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1

    if attempts == 0:
        print(f"\nYou've run out of guesses. You lose. The correct number was {answer}.")
    else:
        print("Guess again.")
