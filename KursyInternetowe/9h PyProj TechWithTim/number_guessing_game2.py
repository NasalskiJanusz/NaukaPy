import random

print("Welcome to Number Guessing Game!")
top_of_range = input("You need to set a top range of number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Sorry, the top range must be greater than zero.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number between 0 and " + str(top_of_range) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("Congrats!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

print("You got it in", guesses, "guesses.")