#napisz funkcję która sprawdzi czy podana liczba to "liczba narcystyczna"


def is_narcissistic(number):
    num_str = str(number)
    num_digits = len(num_str)
    narcissistic_sum = sum(int(digit) ** num_digits for digit in num_str)
    return narcissistic_sum == number

# Test cases
print(is_narcissistic(153))  # Output: True
print(is_narcissistic(1652)) # Output: False