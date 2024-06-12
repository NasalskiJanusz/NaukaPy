# Sprawdzenie Liczby Pierwszej:
# Napisz funkcję, która sprawdza, czy dana liczba jest liczbą pierwszą.
# Liczba pierwsza to liczba większa od 1, która nie ma żadnych dzielników poza 1 i samą sobą.

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False  # Liczba mniejsza lub równa 1 nie jest liczbą pierwszą
    elif liczba == 2:
        return True  # 2 jest liczbą pierwszą
    else:
        # Sprawdzamy czy liczba jest podzielna przez jakąkolwiek liczbę od 2 do pierwiastka kwadratowego z liczby
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                return False  # Jeśli liczba jest podzielna przez inną liczbę niż 1 i sama siebie, to nie jest liczbą pierwszą
        return True

# Przykładowe użycie funkcji:
moja_liczba = 6
if czy_pierwsza(moja_liczba):
    print(moja_liczba, "jest liczbą pierwszą.")
else:
    print(moja_liczba, "nie jest liczbą pierwszą.")
