import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess 1-100: "))
    attempts = attempts + 1

    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print("Correct in", attempts, "attempts")
        break

