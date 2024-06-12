import random
print("Welcome to Rock Paper Scissors!")

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("\nRock, Paper, Scissors or Q to quit! Enter your choice: ").lower()
    if user_choice == "q":
        break

    if user_choice not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]

    if user_choice == computer_choice:
        print("Draw!")
        continue
    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You won!")

    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You won!")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "and computer won", computer_wins)
print("Goodbye!")