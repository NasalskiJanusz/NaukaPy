import os


# there are more arguments that we can pass in:
# 'r' for reading, 'w' for writing
text = "This was overwritten.\n"
text2 = "Have a nice day! See ya\n"

with open('writingInFileExercise.txt', 'w') as file:
    file.write('I just wrote in this file!\n')
    file.write(text)

# if we change our 'text' variable and run this code
# the text that was written in file will be overwritten.
# to avoid this we can change our second argument from writing to appending
# "w" to "a"

with open('writingInFileExercise.txt', 'a') as file:
    file.write(text2)
    file.write(text)