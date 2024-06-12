def czy_parzysta(liczby):
    parzyste, nieparzyste = [], []
    for i in liczby:
        if i % 2 == 0:
            parzyste.append(i)
        else:
            nieparzyste.append(i)
    return parzyste, nieparzyste
def suma(liczby):
    x =0
    for i in liczby:
        x+=int(i)
    return x

liczby = []

while True:
    x = int(input("Podaj liczbe: "))
    liczby.append(x)
    if len(liczby) == 5: break

print(czy_parzysta(liczby))
print(suma(liczby))