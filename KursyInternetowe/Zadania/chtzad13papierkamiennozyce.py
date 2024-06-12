import random

print("Witam w grze 'Papier - kamien - nozyce'")
while True:
    print("Wybierz 1.Papier 2.Nożyce lub 3.Kamien")
    wybor = input("Podaj wybor: ")
    if int(wybor) == 1 or int(wybor) == 2 or int(wybor) == 3:
        if wybor == "1":
            wybor = "Papier"
        elif wybor == "2":
            wybor = "Nozyce"
        else: wybor = "Kamien"
        break
    else:
        print("Wybrałeś inną opcję niż przewiduje program chuju")
        continue


opcje = ["Kamien", "Papier", "Nozyce"]
komputer = random.choice(opcje)


if wybor == komputer: print("Remis")
elif (wybor == "Kamien" and komputer == "Nozyce") or\
    (wybor == "Papier" and komputer == "Kamien")or \
    (wybor == "Nozyce" and komputer == "Papier"):
    print("Wygrałeś!")
else: print("Ciągniesz druta kolego")