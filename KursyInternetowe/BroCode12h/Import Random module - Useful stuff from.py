import random

#gen random number between 1-6
print(random.randint(1,6))

#gen random floating number (between 0 and 1)
print(random.random())

#gen random item from list
myList = ["apple", "banana", "cherry"]
print(random.choice(myList))

#we can shuffle our list (like a deck of cards)
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(cards)
print(cards)


