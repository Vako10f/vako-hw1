import random

def guess_animal():
    animals = ['dog', 'cat', 'lion', 'elephant', 'tiger', 'bear', 'zebra', 'giraffe', 'monkey','tiger','coala','gorrila']
    secret_animal = random.choice(animals)
    attempts = 5

    print("Welcome to Guess the Animal!")
    print("I'm thinking of an animal... Can you guess it?")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()

        if guess == secret_animal:
            print("Congratulations! You've guessed the animal correctly!")
            break
        else:
            print("Incorrect guess! Try again.")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts! The animal was: {secret_animal}")

if __name__ == "__main__":
    guess_animal()

