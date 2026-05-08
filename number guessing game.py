

import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try higher.")
            else:
                print("📉 Too high! Try lower.")

        except ValueError:
            print("❌ Please enter a valid number!")
            continue

    else:
        print(f"\n💥 Game Over! The number was {secret_number}")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        number_guessing_game()

# Run the game
number_guessing_game()
