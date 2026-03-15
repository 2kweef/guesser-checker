import random

secret = random.randint(1, 20)
tries = 0
guess = 0

print("What number am I thinking of between 1 and 20?")


while guess != secret:

    guess = int(input("Please enter a number: "))

    tries = tries + 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You got it in " + str(tries) + " tries!")
