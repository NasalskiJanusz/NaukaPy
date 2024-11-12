import random
import time

def clear_consolex():
    print("\n" * 10)

#DO DOPRACOWANIA
def fight(statsFromPlayer, statsFromEnemy):
    if statsFromPlayer["DEX"] > statsFromEnemy["DEX"]:
        playerAttack = True
        print("You attack first!")
    else:
        playerAttack = False
        print("Enemy starts!")

# Klasy do wyboru
class_names = ["Mage", "Knight", "Archer"]
classes = {
    "mage": {"HP": 75, "STR": 0, "INT": 15, "DEX": 5},
    "knight": {"HP": 150, "STR": 15, "INT": 0, "DEX": 5},
    "archer": {"HP": 100, "STR": 5, "INT": 0, "DEX": 15}
}

# Przedmioty startowe
StartItems = ["potion", "ring", "silver key", "golden nugget", "beer", "flute"]


# Przeciwnicy
Enemies = {
    "training manequin": {"HP": 100, "STR": 0, "INT": 0, "DEX": 0},
    "goblin": {"HP": 100, "STR": 0, "INT": 0, "DEX": 25},
    "banshee": {"HP": 120, "STR": 0, "INT": 20, "DEX": 0},
    "zombie": {"HP": 150, "STR": 15, "INT": 0, "DEX": 0},
    "skeleton": {"HP": 75, "STR": 0, "INT": 0, "DEX": 15},
}

# Wybrana klasa
PlayerStats = {"HP": 0, "STR": 0, "INT": 0, "DEX": 0}
PlayerItems = []

# Powitanie
name = input("What is your name? ").capitalize()
clear_consolex()
print(f"{name}, welcome to adventure!")
print("You need to pick your class first. You can choose from below.")

# Wypisanie wszystkich klas
for index, class_name in enumerate(class_names, start=1):
    print(f"{index}. {class_name}")
print("\n\n\n\n")

# Zmuszenie do wyboru klasy
while True:
    chosen_class_index = input("Enter the number of the class you want to choose: ")
    if chosen_class_index.isdigit():
        chosen_class_index = int(chosen_class_index)
        if 1 <= chosen_class_index <= len(class_names):
            chosen_class = class_names[chosen_class_index - 1].lower()
            PlayerStats = classes[chosen_class]
            clear_consolex()
            print(f"You have chosen {chosen_class.capitalize()} class.\n")
            break
    print("Invalid class choice. Please choose again.")

# Wydruk aktualnych statystyk gracza
print("Your stats are now:")
for stat, value in PlayerStats.items():
    print(f"{stat}: {value}")
print("\n\n")

# Wybieranie przedmiotów początkowych
time.sleep(2)
input("Click ENTER to continue.")
clear_consolex()

# Wybór przedmiotów początkowych
items_to_choose = 3  # Użytkownik może wybrać 3 przedmioty na start
while len(PlayerItems) < items_to_choose:
    print(f"Choose starting items ({items_to_choose - len(PlayerItems)} left):")
    for index, item in enumerate(StartItems, start=1):
        print(f"{index}. {item.capitalize()}")
    print("\n\n")
    choosen_start_item_index = input("Enter the number of the item you want to choose: ")
    clear_consolex()
    if choosen_start_item_index.isdigit():
        choosen_start_item_index = int(choosen_start_item_index)
        if 1 <= choosen_start_item_index <= len(StartItems):
            choosen_start_item = StartItems[choosen_start_item_index - 1].lower()
            if choosen_start_item not in PlayerItems:
                PlayerItems.append(choosen_start_item)
            else:
                print("You have already chosen this item. Please choose another one.")
        else:
            print("Invalid item number. Please choose again.")
    else:
        print("Invalid input. Please enter a number.")

print("Your equipment:")
for item in PlayerItems:
    print(item.capitalize())
print("\n\n\n\n\n")
time.sleep(5)
clear_consolex()

print("Let us begin!\n\n")
print("\n\n\n\n\n\n")
time.sleep(3)
clear_consolex()

print(f"Sir Jamie: {name}! Your hometown was attacked by Hemlock!\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to continue.")
print("Sir Jamie: He is king of goblins who really likes to rob and murder...\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to continue.")
clear_consolex()
print(f"Sir Jamie: You are the best {chosen_class} this world knows!\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to continue.")
print("Sir Jamie: Only You can defeat him!\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to start the journey.")
clear_consolex()

print(f"{name}: When did I fight last time...\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to continue.")
clear_consolex()
print(f"{name}: It was long time ago, I can not even remember when...\n\n\n\n\n\n\n\n\n")
time.sleep(2)
input("Click ENTER to continue.")
clear_consolex()
print(f"{name}: Oh! I can see manequin, It should not be that hard.\n\n\n\n\n\n\n\n\n")
time.sleep(2)
clear_consolex()

# Rozpoczęcie walki z manekinem
