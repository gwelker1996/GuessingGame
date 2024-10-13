import random

def display_heading():
    print("Welcome to the Guessing Game!")

def play_game(limit):
    # Generate a random number between 1 and the user-defined limit
    secret_number = random.randint(1, limit)
    print(f"I have chosen a number between 1 and {limit}. Can you guess?")

    while True:
        # Get user input
        guess = int(input("Enter your guess: "))
        
        # Compare the user guess to the generated random number
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    
    return input("Do you want to play again? (y/n): ").lower() == 'y'


# Example of running the game
if __name__ == "__main__":
    display_heading()
    while True:
        limit = int(input("Enter the upper limit for the guessing game: "))
        if not play_game(limit):
            print("Thanks for playing!")
            break