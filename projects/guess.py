import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        
        if guess.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

if __name__ == "main":
    play_game()