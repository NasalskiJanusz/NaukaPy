# Analiza Tekstu:
# Napisz program, który przyjmuje tekst jako wejście od użytkownika i wykonuje następujące czynności:
# Liczy liczbę słów w tekście.
# Liczy liczbę zdań w tekście.
# Zlicza wystąpienia poszczególnych liter w tekście.
# Zlicza wystąpienia poszczególnych słów w tekście.


def słowa(wszystko):
    return len(wszystko.split(" "))
def zdania(wszystko):
    return len(wszystko.split("."))-1

wszystko = input("Wpisz zdanie/a: ")
print(słowa(wszystko))
print(zdania(wszystko))