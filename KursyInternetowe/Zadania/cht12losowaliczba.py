import random

print("Zagrajmy w gre! Ty podajesz zakres liczb, ja ją losuje a ty próbujesz ją potem znaleźć!")
liczba = input("Podaj liczbe: ")

lista = []
for i in range(int(liczba)):
    lista.append(i+1)
print(lista)
wylosowana_liczba = random.choice(lista)


while True:
    x = input("Podaj liczbe: ")
    if int(x) == int(wylosowana_liczba):
        print("Wygrałeś!")
        break
    elif int(x)>int(wylosowana_liczba):
        print("Twoja liczba jest większa od szukanej.")
    else:
        print("Twoja liczba jest mniejsza od szukanej.")