print("Welcome to my quiz game!")
score = 0

playing = input("Do You want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay, let's play a game!")






answer = input("What does AK stand for? ")
if answer.lower() == "armia krajowa":
    print("Correct!")
    score += 1
else:
    print("Inccorect!")

answer = input("What does Py stand for? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Inccorect!")

answer = input("Who is president of Poland? ")
if answer.lower() == "andrzej duda":
    print("Correct!")
    score += 1
else:
    print("Inccorect!")

answer = input("Who invaded UKR? ")
if answer.lower() == "russia":
    print("Correct!")
    score += 1
else:
    print("Inccorect!")

print("Quiz ended.")
print("Your score was: "+ str(score) + ". I hope you enjoyed my game!")