# module = a file containing python code. May contain functions, classes, etc.
# used wit modular proggraming, which is to separate a program into parts

# after we create a .py file with our code, we need to import it to our main project
import moduleExercise

# to use any function from our other .py file we need to:
# use name of our file then "." and name of the function:
moduleExercise.hello()
moduleExercise.bye()

print("\n")

# to make coding faster we can use alias
import moduleExercise as msg
# now we can use our function like below:
msg.hello()
msg.bye()

print("\n")
# we can also import specific functions from our file:

from moduleExercise import hello,bye

# now we dont need to start from calling our file name, we just call function name:
hello()
bye()

# in some situations we can import all of our functions:
# from moduleExercise import *
# not recommended if You are working on a large program or something that contains many modules
# it may cause name problems (functions may have same name in 2 different files)




# Python has many pre-written modules
# to check them you can:
help("modules")


















