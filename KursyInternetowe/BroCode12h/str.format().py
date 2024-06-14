# --------------------------------------str.format()-----------------------------------------

# str.format() = optional method that gives users more control when displaying output

# example:

# animal = "cow"
# item = "moon"

# print("The " + animal+" jumped over the " + item+".")
# there is better way to display it (using fomrat method):
# we need to use {} as a placeholders

# print("The {} jumped over the {}.".format("cow", "moon"))

# on the end of string we need to use method .format()
# we also need to give variables to this method or just type in anything we want
# REMEMBER! order of given variable matters


# there is second way to display this string:

# print("The {0} jumped over the {1}.".format(animal, item))

# it's called positional arguments
# we just show python where to put our variables in this string

# last way to display string:

# print("The {item} jumped over the {animal}.".format(animal = "cow", item = "moon"))

# we have shown python where to put our variables but
# in this case we used keyword argument to do this
# REMEMBER! You can use one keyword more than once, example:

# print("The {item} jumped over the {item}.".format(animal = "cow", item = "moon"))
#it also works with positional arguments

# there is even better way to write this code, more elegant way:

# text = "The {} jumped over the {}."
# print(text.format(animal, item))

# we made variable that has our string to display (with placeholders)
# all we need to do is print it out and add .format with arguments

            # ADDING PADDING

# name2 = "Janek"
# print("Hello, my name is {:10}. Nice to meet you.".format(name2))
#
# # when we print it out, we gave "10 spaces" of length reserved for our argument
# # ten spaces worth of room
#
# # we alco can left/center/right align it, to do this:
# print("Hello, my name is {:<10}. Nice to meet you.".format(name2))  #left
# # output: Hello, my name is Janek     . Nice to meet you.
#
# print("Hello, my name is {:>10}. Nice to meet you.".format(name2))  #right
# # output: Hello, my name is      Janek. Nice to meet you.
#
# print("Hello, my name is {:^10}. Nice to meet you.".format(name2))  #center
# # output: Hello, my name is   Janek   . Nice to meet you.
#
# #dont forget that we still can use our positional argument/key word argument:
# print("Hello, my name is {0:<10}. Nice to meet you.".format(name2))
# print("Hello, my name is {name:<10}. Nice to meet you.".format(name2))

        #FORMATING NUMBERS

# number = 3.14159

# to display only 2 digits after . we need to:

# print("The number pi is {:.2f}".format(number))     #output: The number pi is 3.14
# !!!!keep in mind that this method will round your number!!!!

# number2 = 1000
# how to add "," to make numbers look better:
# print("The number pi is {:,}".format(number2))

# how to make binary/oct/hex/scientific notation representation of our number:
# print("The number pi is {:b}".format(number2))
# print("The number pi is {:o}".format(number2))
# print("The number pi is {:x}".format(number2))  #lower x if we want letthers to be lower, opposite to X
# print("The number pi is {:E}".format(number2))  #same thing as with hex case, SIZE MATTERS ;P
