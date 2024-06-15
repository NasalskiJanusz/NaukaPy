# Pętle i listy:
# Napisz program, który przyjmuje od użytkownika liczbę całkowitą n i wyświetla wszystkie liczby całkowite od 1 do n.
# Napisz program, który przyjmuje od użytkownika listę liczb i zwraca listę zawierającą tylko parzyste liczby z pierwotnej listy.


# function to make a list from 1 to n
def from0toN(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list

# function that returns only not odd numbers from list
def notOddNumbers(list):
    listNotOdd = []
    for i in list:
        if i % 2 == 0:
            listNotOdd.append(i)
    return listNotOdd

#---------------------------------------------------------------

# user n input
user = input("Enter number that will be end of our range: ")
user = int(user)
# print list from "from0toN" function
print("Numbers from 1 to "+str(user)+ ":\n"+str(from0toN(user))+"\n")
# print list with only not odd numbers
print("Not odd numbers in this list are:\n"+str(notOddNumbers(from0toN(user))))







