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



#-----------------------------------------------------------END STATEMENTSs-------------------------------------------
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











