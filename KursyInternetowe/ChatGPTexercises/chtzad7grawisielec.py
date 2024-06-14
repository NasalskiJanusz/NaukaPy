# # Gra w wisielca:
# # Stwórz prostą grę w wisielca. Program losuje słowo, a gracz ma za zadanie odgadnąć to słowo, podając litery.
# # Gracz ma określoną liczbę prób na odgadnięcie słowa.
import random

slowa = ['kot', 'kutas', 'cipa', 'anal', 'cycki', 'wagina', 'stara', 'grzybiarz']
zycia = 10
wylosowane_slowo = random.choice(slowa)
zgadywane_slowo = "_"*len(wylosowane_slowo)

for i in range(zycia):
    print("Zgadywane słowo: "+zgadywane_slowo)
    print("Pozostało ci " + str(zycia) + " żyć/a/e.")
    literka = input("Podaj literkę: ")

    if str(zgadywane_slowo) == str(wylosowane_slowo):
        print("Wygrałeś!")
        break
    elif literka in wylosowane_slowo:
        print("Zgadłeś literke.")
        z = wylosowane_slowo.index(literka)                   #index znalezionej literki
        zgadywane_slowo = zgadywane_slowo[:z] + literka + zgadywane_slowo[z + 1:]
        continue
    else:
        zycia -= 1







#TO NA DOLE ZROBIŁ CHAT GPT

# import random
#
# def wylosuj_slowo():
#     slowa = ["python", "programowanie", "komputer", "internet", "ananas"]
#     return random.choice(slowa)
#
# def gra_w_wisielca():
#     slowo = wylosuj_slowo()
#     dlugosc_slowa = len(slowo)
#     zgadniete = ['_'] * dlugosc_slowa
#     proby = 7
#
#     print("Witaj w grze w wisielca!")
#     print("Odgadnij słowo. Ma ono", dlugosc_slowa, "liter.")
#     print("Masz", proby, "prób.")
#
#     while proby > 0 and '_' in zgadniete:
#         print(" ".join(zgadniete))
#         litera = input("Podaj literę: ").lower()
#
#         if len(litera) == 1 and litera.isalpha():
#             if litera in slowo:
#                 for i in range(dlugosc_slowa):
#                     if slowo[i] == litera:
#                         zgadniete[i] = litera
#             else:
#                 proby -= 1
#                 print("Nie ma takiej litery. Pozostało prób:", proby)
#         else:
#             print("Podaj jedną literę!")
#
#     if '_' not in zgadniete:
#         print("Gratulacje! Odgadłeś słowo:", slowo)
#     else:
#         print("Przegrałeś! Szukane słowo to:", slowo)
#
# # Uruchomienie gry
# gra_w_wisielca()
