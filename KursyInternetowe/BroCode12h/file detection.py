# basics of import os

# first of all we need to import os
import os

# with this module we can do many things, for example checking if specific file exists in given location
# to check it we need a path:


# if you can see orange text, you should change single "/" into double "//"
path = "C:\\Users\\Janek\\Desktop\\ProjektyPy\\KursyInternetowe\\BroCode12h\\fileDetectionExercise.txt"

# we are checking if this paths exists
if os.path.exists(path):
    print("That location exists!")
    # here we are checking if this is a file
    if os.path.isfile(path):
        print("That is a file!")
    # here we are checking if this is directory (folder)
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location does not exist!")