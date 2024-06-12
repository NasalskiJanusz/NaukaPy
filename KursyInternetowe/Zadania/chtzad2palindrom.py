# Palindrom Checker:
# Napisz funkcję, która sprawdza, czy dany ciąg znaków jest palindromem.
# Palindrom to ciąg znaków, który czytany od przodu i od tyłu brzmi tak samo.Przykłady palindromów: "radar", "kajak", "anna"

def palindrome(word):
    return word[::-1] == word

print(palindrome("kajak"))