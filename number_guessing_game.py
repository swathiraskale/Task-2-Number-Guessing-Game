import random

secret_number = random.randint(1, 100)
attempts = 0

print("===================================")
print("     NUMBER GUESSING GAME")
print("===================================")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = input("\nEnter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number:", secret_number)
        print("Total attempts:", attempts)
        break
