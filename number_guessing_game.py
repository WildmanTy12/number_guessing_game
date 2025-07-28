import random

while True:
    hint = " "
    tries = 0
        
    print("Welcome to the number guessing game! \n I'll pick a number from 0 to 100, can you try guess it correctly before running out of guesses?")

    #Select difficulty
    while True:
        try:
            difficulty = int(input("Pick a difficulty:  \n 1. Easy - 10 attempts \n 2. Medium - 5 attemps \n 3. Hard - 3 attempts: "))

            if difficulty == 1:
                attempts_allowed = int(10)
                print(f"You've selected Easy, you have {attempts_allowed} attempts to guess my number, piece of cake!")
                break

            elif difficulty == 2:
                attempts_allowed = int(5)
                print(f"You've selected Medium, you have {attempts_allowed} attempts to guess my number, you got this!")
                break

            elif difficulty == 3:
                attempts_allowed = int(3)
                print(f"You've selected Hard, you have {attempts_allowed} attempts to guess my number, good luck!")
                break

            else:
                print("Please enter a valid number (1, 2, or 3). Try again!\n")
                
        except ValueError:
            print("Please enter a valid number (1, 2, or 3). Try again!\n")

    secret_num = random.randint(0, 100)
    #Game begin
    # First guess input
    while True:
        try:
            guess = int(input(f"\nGame start! I've selected a number between 0 and 100.\nWhat is your first guess?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

    # First guess logic
    if guess == secret_num:
        print(f"Correct, it was {secret_num}! You win on the first try! 🎉")
    else:
        tries = 1  # first guess counted
        while guess != secret_num:
            if tries >= attempts_allowed:
                print(f"You lose, it was {secret_num}")
                break

            if guess < 0 or guess > 100:
                print("Out of bounds! Please enter a number between 0 and 100.")
            elif guess < secret_num:
                hint = "higher"
            elif guess > secret_num:
                hint = "lower"

            remaining_guesses = attempts_allowed - tries
            print(f"Incorrect, it is {hint} than {guess}. You have {remaining_guesses} guesses left.")

            # Get next guess
            try:
                guess = int(input("What is your next guess?: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            tries += 1
        else:
            print(f"You won! It was {secret_num}, and you finished in {tries} attempts! 🎉")
    play = input("Would you like to play again?: (Yes or No)").lower()
    if play == "no":
        print("Goodbye, see you next time!")
        break
    else: 
        continue