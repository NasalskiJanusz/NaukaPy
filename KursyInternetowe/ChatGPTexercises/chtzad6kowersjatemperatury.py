# Konwersja Temperatury:
# Napisz funkcję, która konwertuje temperaturę z jednostki Celsiusza na Fahrenheit lub odwrotnie. Formuły konwersji:
# Z Celsiusza na Fahrenheit: F = C * 9/5 + 32
# Z Fahrenheita na Celsiusza: C = (F - 32) * 5/9

def FtoC(F):
    return (int(F)-32)*85/9
def CtoF(C):
    return int(C)*(9/5)+32

a = input("Wybierz jednostkę Celcius'a lub Farenheita' (C lub F): ")
b = input("Wpisz temperaturę, którą chcesz przekonwertować: ")

if a == "C" or a == "c": print(CtoF(b))
elif a == "F" or a == "f": print(FtoC(b))
