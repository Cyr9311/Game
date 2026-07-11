import random

secret = random.randint(1, 10)

print("Guess a number between 1 and 10")

while True:
    guess = int(input("Your guess: "))

    if guess == secret:
        print("🎉 You win!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")