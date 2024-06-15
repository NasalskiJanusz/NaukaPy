# Steps:
# 1. define function that will count chars
# 2. make two counters
# 3. define "samogłoski"
# 4. iterate through each 'char' in given string
#       * check if 'char' is letter
#       * if yes, check if it's in "samogłoska" set
#           * if yes += to "samogłoski" counter
#           * if not += to "spółgłoski" counter

# set of 'chars' that we will use to check if samogłoska
setOfSamogloski = set("aeiouyAEIOUY")

# function that will count everything
def counting(string, secik):
    samogłoski = 0
    spółgłoski = 0
    otherChars = 0
    for char in string:
        # if not letter:
        if not char.isalpha():
            otherChars += 1
        # if samogłoska
        elif char in secik:
            samogłoski += 1
        # if spółgłoska
        else:
            spółgłoski += 1
    return samogłoski,spółgłoski,otherChars

# user input string
userInput = input("Enter a string: ")

# saving results from recursive function
funcResult = counting(userInput, setOfSamogloski)

# print results in elegant way
print("In given string we counted: \n\n1. Samogłoski: "+str(funcResult[0])+"\n2. Spółgłoski: "+str(funcResult[1])+"\n3. Other characters: "+str(funcResult[2]))




















