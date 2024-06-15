# function to reverse string
# meaning of [::-1] start:stop:step
def reverseString(string):
    return string[::-1]

theStringToReverse = "Python is awesome!"
theStringAfterReverse = reverseString(theStringToReverse)

# print string before reversing
print(theStringToReverse)
# print reversed string
print(theStringAfterReverse)
print("-------------------------------------------------")

                                                                # additional steps in this exercise:
# 1. ask user for input
# 2. split given sentence
# 3. reverse each word in this sentence
# 4. connect each reversed word into one sentence
# 5. print the result

# function to slice and return the list
def split(string):
    return string.split()

# function to reverse each word in sentence and return list of it
def reverse(string):
    reversedList = []

    # reversing each word then adding it to local list
    for i in string:
        fromTheBack = i[::-1]
        reversedList.append(fromTheBack)
    # capitalizing 1st letter of reversed sentence then adding "." at the end (if there is not)
    reversedList[0] = reversedList[0].capitalize()
    if reversedList[-1] != ".":
        reversedList[-1] += "."
    return reversedList


# function that connects reversed words into one sentence
def connect(string):
    connected = ""
    listPreConnect = []

    # adding to local list
    for word in string:
        listPreConnect.append(word)

    # connecting string variable with local list
    connected = " ".join(listPreConnect)
    return connected

# user input
userInput = input("Enter a sentence to reverse: ")

# saving sentence after splitting by split function
splitted = split(userInput)

# i will capitalize 1st letter and add "." at the end of the sentence if user forgot that
# so i can print his sentence in elegant way
# i'm using split function one more time, it's making program slower.
spltPrint = split(userInput)
spltPrint[0] = spltPrint[0].capitalize()
if spltPrint[-1] != ".":
    spltPrint[-1] = spltPrint[-1] + "."
print("-------------------------------------------------\nYour sentence is now splitted, let's see how it looks like in the list: \n", splitted)
print("-------------------------------------------------")

# saving results of reverse function and printing it
reversed = reverse(splitted)
print("This is your reversed sentence: ")
for i in reversed:
    print(i,end=" ")

print("\n\nAnd how it looks like in the list:\n",reversed)
print("-------------------------------------------------")

# saving result of connect function and printing it
connectedString = connect(reversed)
print("After connection we have one string: ",connectedString)


# I could make it look in more elegant but those are just string exercises :)