#list is used to strone multiple items in a single variable
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



fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits[0] = "kiwi"                          #setting [0] to "kiwi"
fruits.append("orange")                     #adding to list
fruits.append("strawberry")
fruits.append("chicken nuggets")
fruits.insert(1,"lemon")     #adding exactly here
fruits.remove("banana")                     #removing from the list

print(fruits)
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
    print(foods)

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
