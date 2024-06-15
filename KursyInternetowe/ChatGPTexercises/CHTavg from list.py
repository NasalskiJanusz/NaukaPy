#Napisz program, który przyjmuje od użytkownika listę liczb całkowitych i oblicza ich średnią arytmetyczną.

list = []
# user adds 5 numbers to the list
while len(list) < 5:
    x = input("Enter a number: ")
    list.append(int(x))

# function to calculate avg
def average(x):
    # the sum of numbers divided by their number
    return sum(x)/len(x)

print("-----------------------------------\nGiven numbers: "+str(list))
print("-----------------------------------\nThe average is: "+str(average(list)))
















