import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)
    
    # Number of attempts
    attempts = 10

    print(f"Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            continue
            
        if guess == random_number:
            print(f"Congratulations! You've guessed the number {random_number} in {attempt} attempts.")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"Sorry! You've used all {attempts} attempts. The number was {random_number}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
