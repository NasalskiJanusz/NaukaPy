def mnożenie(x,y):
    wynik = int(x) * int(y)
    return wynik
def dzielenie(x,y):
    wynik =int(x) / int(y)
    return wynik
def dodawanie(x,y):
    wynik = int(x) + int(y)
    return wynik
def odejmowanie (x,y):
    wynik = int(x) - int(y)
    return wynik

def kalkulator():
    while True:
        x = input("Podaj pierwszą liczbę: ")
        y = input("Podaj drugą liczbę: ")
        print("Co chcesz zrobić?")
        z = input("1. dodawanie 2. odejmowanie 3. mnożenie 4. dzielenie 5. wprowadź liczby jeszcze raz: ")
        if z=="1":
            print(dodawanie(x,y))
        elif z=="2":
            print(odejmowanie(x,y))
        elif z=="3":
            print(mnożenie(x,y))
        elif z=="4":
            if y == "0":
                print("nie można dzielić przez 0!")
                continue
            else:
                print(dzielenie(x,y))
        elif z=="5":
            continue
        else:
            print("To też przewidziałem!")
            print("Nie tym razem :)")
            continue
kalkulator()

