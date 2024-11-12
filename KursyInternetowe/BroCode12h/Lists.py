#list is used to strone multiple items in a single variable


# List Comprehension offers the shortest syntax for looping through lists:
# Example:
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

'''
List Items
    List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
    Since lists are indexed, lists can have items with the same value:
'''

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Example
# Add elements of a tuple to a list:
#
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


fruits = ["apple", "banana", "cherry"]
print("\n",fruits)

fruits[0] = "kiwi"                          #setting [0] to "kiwi"
fruits.append("orange")                     #adding to list
fruits.append("strawberry")
fruits.append("chicken nuggets")
fruits.insert(1,"lemon")     #adding exactly here
fruits.remove("banana")                     #removing from the list

print("\n",fruits)
print("Last thing in your list is: "+str(fruits[-1])+", using negative indexing.")
print("3tr 4th and 5th in your list is: "+str(fruits[2:5]))
print("Len of this list: "+str(len(fruits)))



# --------------------------------------LIST------------------------------------------

food = ['apple', 'banana', 'hamburger', 'grape', 'watermelon']


food.append('orange')                   #dodanie do listy
food.remove("apple")                    #usuwanie z listy
food.pop()                              #usuwa ostatnią daną z listy (ostatni index)
food.insert(0,'cake')    #dodaje do listy w wytyczonym indexie
food.sort()                             #sortowanie alfabetycznie
food.clear()                            #usuwa elementy listy

for foods in food:
    print("\n",foods)

# --------------------------------------2D-LIST------------------------------------------
#o ile pamiętam to były macierze
#
# drinks = ['coffee','milk','soda']
# desserts = ['cake','ice cream']
# dinners = ['pizza', 'hamburger', 'spaghetti']
#
# food = [drinks, desserts, dinners]
#
# print(food[0])      #wyświetli tylko listę drinks (w zależności od indeksu
# print(food[2][2])   #wyświetli tylko 3 element trzeciej listy

#-----------------------------------------------------------COMPREHENSION-------------------------------------------


# elegant way to make new list based on existing one
# long way to solve exercise:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("\n",newlist)

# short way to do this using comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("\nComprehension use:\n",newlist)

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

#-----------------------------------------------------------COMPREHENSION-------------------------------------------
#
#
# you can sort list descending (reversed)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print("\nReversed sorting:\n",thislist)
#
# You can also customize your own function by using the keyword argument key = function.
# Example:
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("\nCustom functions used with sorting:\n",thislist)
#
# Sometimes sort can make unexpected results
# for example: capital letters are being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("\nUnexpected result:\n",thislist)
#
# luckly we can use built-in functions as key functions when sorting a list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print("\nAfter using .lower as a key function in sorting:\n",thislist)
#
# Reverse order:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("\nPre reverse() method:\n",thislist)
thislist.reverse()
print("\nReverse() on list result:\n",thislist)
#
#
#
#

