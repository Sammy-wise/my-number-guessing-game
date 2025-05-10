#It should choose a random number between 1 and 100, then challenge the player to guess the number in 10 turns.
# After each turn the player should be told if they are right or wrong, and if they are wrong,
# whether the guess was too low or too high. It should also tell the player what numbers they previously guessed.




from time import sleep
import random



def greeting():
    print("Helo! Welcome to the guessing game")
    print('Loading...')
    sleep(2)
    name = (input('Please enter your name to start the game:'))
    print("welcome "+name)
    print('Loading...')
    sleep(2)





def guessing():
    key = random.randint(1, 100)
    try:
        for i in range(10):
            guess = input("Enter your next number:")
            if guess == key:
                print("CONGRATS, YOU'VE WON THE GAME!!!!")
            elif:
                if guess > key:
                    print("Sorry, your guess is too high.")
            elif guess < key:
                print("Sorry, your guess is too low.")
                break
            else:
                continue
    except:
        if guess > key:
            print("Sorry, your guess is too high.")





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



    return key

guessing()
