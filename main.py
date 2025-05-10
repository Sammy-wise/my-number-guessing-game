#It should choose a random number between 1 and 100, then challenge the player to guess the number in 10 turns.
# After each turn the player should be told if they are right or wrong, and if they are wrong,
# whether the guess was too low or too high. It should also tell the player what numbers they previously guessed.

from mymodule import *
print("Loading...")
sleep(2)
greeting()
rules()
numbers = list(range(1, 101))
try:
    for i in range(10):
        if key() == guessing():
            break
        print("CONGRATS, YOU'VE WON THE GAME!!!!")
finally:
    pass