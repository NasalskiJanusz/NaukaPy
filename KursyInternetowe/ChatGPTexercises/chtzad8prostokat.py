# Tworzenie Prostokąta z Znaków:
# Napisz funkcję, która przyjmuje dwie liczby całkowite (szerokość i wysokość).
# Niech drukuje prostokąt zbudowany z określonych znaków, na przykład "*".



def rysuj_prostokat(szerokosc, wysokosc, znak='*'):
    for i in range(wysokosc):
        for j in range(szerokosc):
            print(znak, end='')
        print()

# Przykładowe wywołanie funkcji
szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))

rysuj_prostokat(szerokosc, wysokosc)
