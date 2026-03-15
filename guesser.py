import random

secret = random.randint(1, 20)
tries = 0
guess = 0

print("What number am I thinking of between 1 and 20?")
text = input("Take a guess: ")

guess = int(text)
tries = tries + 1

if guess == secret:
    print("Correct")
else:
    text = input("Incorrect, try again: ")
