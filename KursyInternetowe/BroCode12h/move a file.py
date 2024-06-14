import os

source = "C:\\Users\\Janek\\Desktop\\ProjektyPy\\KursyInternetowe\\BroCode12h\\MovingExercise\\moveFileExercise.txt"
destination = "C:\\Users\\Janek\\Desktop\\ProjektyPy\\KursyInternetowe\\BroCode12h\\MovingExercise\\1st destination\\moveFileExercise.txt"

source2 = "C:\\Users\\Janek\\Desktop\\ProjektyPy\\KursyInternetowe\\BroCode12h\\MovingExercise\\moveFileExercise2.txt"
destination2 = "C:\\Users\\Janek\\Desktop\\ProjektyPy\\KursyInternetowe\\BroCode12h\\MovingExercise"


# it's always better to make exceptions

try:
    # we are checking if there is already file with the same name
    if os.path.exists(destination):
        print("There is already a file there")
    # if there is no we are moving our file
    else:
        os.replace(source, destination)
        print("The file has been moved")
except FileNotFoundError:
    print("File not found.")


