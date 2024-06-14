import os
import shutil

# you can handle it in two ways:
# 1. make a variable with path
# 2. set path in method

path = 'deletingExercise.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found.")

# os.remove() does not remove empty folders, os.rmdir() does
# if we try to delete folder with os.remove() error will be shown: PermissionError
# this is how to do so:

pathToFolder = 'deleteMe'

try:
    os.rmdir(pathToFolder)                  #remove directory
except FileNotFoundError:
    print("This directory was not found.")
# we get PermissionError, let's make exception
except PermissionError:
    print("You do not have permission to delete this directory.")
else:
    print("Deleted!")

# That function does not remove directory with files inside of it
# if we try to delete folder with files inside using os.rmdir() error will be shown: OSError
# this is how to do so, we need shutil.rmtree():

pathToFolderWithFiles = 'deleteMeWithFiles'

try:
    # REMEMBER! it's dangerous, because this function deletes directory + files.
    # May cause problems...
    shutil.rmtree(pathToFolderWithFiles)
except FileNotFoundError:
    print("This directory was not found.")
# if we use os.remove() to delete empty folder
except PermissionError:
    print("You do not have permission to delete this directory.")
# if we use os.rmdir() to delete directory with file inside
except OSError:
    print("You can not delete that using that function.")
else:
    print("Deleted!")


