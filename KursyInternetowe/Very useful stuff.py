#--------------------------------------------------------------MAP-------------------------------------------
# MAP
# in Python map() applies a function to each iterable
# like a list, tuple or set and returns an iterator of the results.
# example:
print("-----------------------------------------map()----------------------------------------------")
stringListToMap = ["1", "2", "3", "4", "5"]
# lets print list and type of data for index [0]
print("The list: "+str(stringListToMap))
print("The type of 1st date with [0] index inside the list pre mapping is: "+str(type(stringListToMap[0])))
# use of map(), for each i in "stringListToMap" we change str to int
numbersAfterMapping = list(map(int, stringListToMap))
print("This is your list: "+str(numbersAfterMapping)+".\nAnd this is type of 1st date with [0] index inside the list after mapping: "+str(type(numbersAfterMapping[0]))+".")



#-----------------------------------------------------------ISALPHA()-------------------------------------------

print("\n-----------------------------------------isalpha()----------------------------------------------")
# this method is checking if there are only letters (a-z and A-Z)
# it will return 'True' if there is anything else than letters (numbers, spaces or special chars)

# example:

# function to check it:
def anythingElseCheck(x):
    for char in x:
        if not char.isalpha():
            return True  # Found some not-letter character
    return False  # All characters are letters

# samples:
exampleIsAlpha1 = "I have 22 years old."
exampleIsAlpha2 = "Janusz"

# print variable
print("1. Variable that we will check with isalpha() method: '"+str(exampleIsAlpha1)+"'.")
print("2. Variable that we will check with isalpha() method: '"+str(exampleIsAlpha2)+"'.")
# isalpha() to check:
print("\nIf you see 'True' - no letter character found, else there are only letters.\n")
print("Results are as follows: ")
print("1. "+str(anythingElseCheck(exampleIsAlpha1)))
print("2. "+str(anythingElseCheck(exampleIsAlpha2)))

# in 1. variable there are spaces, numbers and "." that counts as special character
# in 2. we have only letters (it does not matter if they are upper or not)



#-----------------------------------------------------------END STATEMENTS-------------------------------------------
print("\n-----------------------------------------end='' statement----------------------------------------------")

exampleList = ["Hi", "there", "buddy."]
print("Example list that we are working on: ", exampleList, end="\n\n")
# when we print it using for loop:
print("The results are as follows:")
for example in exampleList:
  print(example)

# Results:
# Hi
# there
# buddy.

print("\n1. Slash n result: ")
for example in exampleList:
  print(example, end="\n")
print("\n2. Slash t result: ")
for example in exampleList:
  print(example, end="\t")
print("\n\n3. Space result: ")
for example in exampleList:
  print(example, end=" ")
print("\n\n4. Anything else we choose result: ")
for example in exampleList:
  print(example, end=">>>")
# to make it one line print we can add end statement
# end statement can take values as follows:
# 1. end=''         there won't be any changes
# 2. end='\n'       each print with that value will be printed in the new line
# 3. end=' '        each print space is added at the end
# 4. end='>>>'      character that we picked will be printed at the end of print
# 5. end='\t'       adds "TAB" at the end of print with that value


#-----------------------------------------------------------FILTER-------------------------------------------
print("\n-----------------------------------------filter()----------------------------------------------")

# nice way to execute function:
def is_even(x):
    return x % 2 == 0
my_list = [1,2,3,4,5,6,7,8,9]

# just use filter method
# this method is used to process a sequence (list, tuple, etc.)
# it returns elements that satisfy specific conditions
# it takes two arguments:
# (Function that returns True or False and Sequence of elements)

result = filter(is_even, my_list)
print(list(result))


#-----------------------------------------------------------COMPREHENSION-------------------------------------------
print("\n-----------------------------------------comprehension----------------------------------------------")
# elegant way to make new list based on existing one
# long way to solve exercise:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# short way to do this using comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# benefits? 3 lines instead of 6, looks more elegant way
# The Syntax:
'''newlist = [expression for item in iterable if condition == True]'''
# expression - current item in the iteration AND also the outcome
# FOR item IN iterable - simple for loop to go through the list
# IF condition == TRUE - (optional) element will be added in new list if...
#
# Other cool things about this topic:
#
# you can use range to iterate
'''newlist = [x for x in range(10)]'''
#
# you can manipulate expression (current item in the iteration):
'''newlist = [x.upper() for x in fruits]'''
#
# expression can also contain conditions, not like a filter, but as a way to manipulate the outcom
'''newlist = [x if x != "banana" else "orange" for x in fruits]''' # returns "orange" instead of "banana"
#
#
#
#
#
#
#
#
#

