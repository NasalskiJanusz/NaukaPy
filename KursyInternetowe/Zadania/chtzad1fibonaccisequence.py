# Fibonacci Sequence:
# Napisz funkcję, która generuje ciąg Fibonacciego dla danej liczby n. Ciąg Fibonacciego zaczyna się od 0 i 1,
# a każda kolejna liczba w ciągu jest sumą dwóch poprzednich liczb.Przykładowy wynik dla n = 10:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(n):
    a, b = 0, 1
    z = []
    for value in range(n):
        z.append(a)
        a, b = b, a + b
    print(z)

fibonacci(10)