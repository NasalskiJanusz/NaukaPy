import os

# If your file or directory is in this same place as your project
# you are not obligated to give full path to this file/directory

# with open("readingFileExercise.txt") as file:
#     print(file.read())

# you just read what is inside this file!
# also, this code closes this file right after reading
# to chceck it we can use:

# print(file.closed)        #returns True/False


# we should add some exceptions that are going to handle errors


try:
    with open("readingFileExercise.txt") as file:
        print(file.read())
# if there is not file:
except FileNotFoundError:
    print("That file was not found.")




