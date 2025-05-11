#It should choose a random number between 1 and 100, then challenge the player to guess the number in 10 turns.
# After each turn the player should be told if they are right or wrong, and if they are wrong,
# whether the guess was too low or too high. It should also tell the player what numbers they previously guessed.




from time import *
import random
import time



def greeting():
    print("Helo! Welcome to the guessing game")
    print('Loading...')
    sleep(2)
    name = (input('Please enter your name to start the game:'))
    print("welcome "+name)
    print('Loading...')
    sleep(2)




def guessing():
    key = random.randint(1, 101)  # You can remove this line in actual game
    start_time = time.time()  # Start the timer

    for i in range(10):
        try:
            guess = int(input("Enter your next number (1-100): "))
            if guess < 1 or guess > 100:
                print("Your guess is out of range. Please guess between 1 and 100.")
                continue
            if guess == key:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"CONGRATS, YOU'RE CORRECT AND YOU'VE WON THE GAME in {duration} seconds!")
                break
            elif guess > key:
                print("Sorry, your guess is too high.")
            else:
                print("Sorry, your guess is too low.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Game over. You've used all 10 guesses.")
        print(f"The correct number was {key}.")





def rules():
    rule = (
        "Guess the Number Game Rules:\n"
        "- A random number between 1 and 100 will be selected.\n"
        "- You have 10 chances to guess it.\n"
        "- After each guess, you'll be told if it's too high, too low, or correct.\n"
        "- You'll also see all your previous guesses.\n"
        "- The game ends if you guess right or use all 10 turns."
    )
    print(rule)
    print("Loading...")
    sleep(5)





