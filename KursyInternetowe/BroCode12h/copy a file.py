# there are multiple ways to do this.
# dude from course suggested to import shutil

import shutil

# there are 3 basic functions to copy a file
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

# in this function there are 2 arguments: source and destination
# but we can just change name of this file:
shutil.copyfile('copyExercise.txt', 'copyOfcopyExercise.txt')

# you can copy your file to any other destination (it it does exists)
# to do this just add destination insted of name







