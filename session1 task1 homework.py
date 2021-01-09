import random

number: int = random.randint(1, 10)

print("Hello, I am a random number guessing game!")
user_input = input ("What is your name?")

print("Hello", user_input, "Let's play a game!  I'm thinking of a number between 1 and 10, try and guess what it is!")

guess = int
while guess != number:

    guess = int(input("What number do you guess?"))

    if guess < number:
        print("Too low, try again.")

    elif guess > number:
        print("Too high, try again.")

if guess == number:
    print("Smarty pants! You guessed correctly! The number was", number, "!")










