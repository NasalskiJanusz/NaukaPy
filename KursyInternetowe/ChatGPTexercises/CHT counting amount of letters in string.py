# Steps:
# 1. make function that will count amount of specific letter appearing
# 2. make dictionary and call it as you like
# 3. iterate trough each 'char' in given string:
    # * ignore spaces (' ') and other chars that are not letters
    # * make every character in lower
    # * if character is already in dictionary, find its key and add +1 to his value
    # * if character is not yet in dictionary, add it and set value to 1
# print dictionary

def countLetters(string):
    # lowering string
    string=string.lower()

    # dictionary that will save data of letters
    dictionary = {}

    # for loop to check if letter is already in dict
    # if yes we add +1 to value, if not we add letter to dict
    for i in string:
            # skip all spaces
            if i == " ":
                continue
            # if character is not letter > skip
            elif not i.isalpha():
                continue
            elif i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
    return dictionary


# string from the user
userInput = input("Enter a string: ")

# saving results of countLetters function
countedDict = countLetters(userInput)

# 1st way to print it:
print("1st way to print results (whole dictionary): \n"+str(countedDict))

# 2nd way to print it:
print("\n2nd way to print results (looping through all keys and their values): ")
for key, value in countedDict.items():
    print(str(key) + ": " + str(value), end="\t")














