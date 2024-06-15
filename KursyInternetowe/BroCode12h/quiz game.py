#-----------------------------------
def new_game():
    # user answers:
    guesses = []
    # user score:
    correct_guesses = 0
    # question number:
    question_num = 1

    # showing questions for user:
    for key in questions.keys():
        print("-----------------------------------")
        print(key)
        # we need to display possible answers:
        # to avoid showing all list with answers each question we will use indexing:
        # -1 is because python starts counting from 0
        for i in options[question_num-1]:
            print(i)

        # now we add user input:
        guess = input("Enter (A, B, C, D): ")
        # let's make it upper in case user forgets to do so:
        guess = guess.upper()
        # now let's add it to the guesses list:
        guesses.append(guess)

        # now we need to check if the answer was correct
        # we call our function with those arguments:
        # 1. questions.get(key) - questions dictionary > go to key > get value of key (correct answer)
        # 2. user guess, so we can check his answer with dictionary answer
        # we also are executing this function in += correct_guesses,
        # so we can automatically add points if user guess returns 1 or 0
        correct_guesses += check_answer(questions.get(key), guess)

        # incrementation of question number
        question_num += 1

    # now we will display users final score
    # NOTE! do it after iteration of for loop (after all questions was answered)
    display_score(correct_guesses, guesses)

# -----------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

#-----------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------")
    print("RESULTS")
    print("-----------------------------------")
    print("Correct answers: ", end="")

    # we are iterating trough questions dictionary,
    # we are printing only value that is connected to the i key
    for i in questions:
        print(questions.get(i), end=" ")
    print("")

    # now we are iterating trough user answers
    print("Your guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print("")

    # we should output total score
    # we are dividing correct guesses by amount of questions
    # then we multiply it by 100
    score = int((correct_guesses/len(questions))*100)
    # we print score as %
    print("Your score is: "+str(score)+"%")

#-----------------------------------
def play_again():
    a = input("Would you like to play again? (Y/N): ")
    a = a.upper()
    if a == "Y":
        return True
    else:
        return False



# questions for our quiz
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which group?: ": "C",
    "Is the Earth round?: ": "A"
}
# all possible answers to our questions
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckenburg"],
           ["A. 1989", "B. 1991", "C. 200", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]



# starting game
new_game()

# asking if user wants to play again
while play_again():
    new_game()

# bye
print("\n\nByeee!")






