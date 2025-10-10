import random

secret_number = random.randint(1, 100)
guess_count = 0

while True:
    guess_count += 1
    guess = int(input("Guess the number (1-100): "))
    if guess < secret_number:
        print("Too low,try again.")
    elif guess > secret_number:
        print("Too high,try again.")
    else:
        print(f"You got it in {guess_count} guesses!")
        break