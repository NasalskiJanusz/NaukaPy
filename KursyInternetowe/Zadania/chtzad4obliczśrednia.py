# Obliczanie Średniej:
# Napisz funkcję, która oblicza średnią arytmetyczną z listy liczb.

# dodaj kazda liczbe do siebie i podziel przez ich ilość

def srednia(lista):
    if not lista:
        return None  # Zwraca None, jeśli lista jest pusta
    else:
        return sum(lista) / len(lista)

# Przykładowe użycie funkcji:
moja_lista = [1, 2, 3, 4, 5]
print("Średnia arytmetyczna:", srednia(moja_lista))
