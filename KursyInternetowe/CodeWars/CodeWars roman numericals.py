# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
#
# Example:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      ->  400
# "XC"      ->   90
# "XL"      ->   40
# "I"       ->    1
# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def roman_to_int(roman):
    # Dictionary to map Roman numerals to their values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the integer value
    total = 0
    prev_value = 0

    # Iterate over each character in the Roman numeral string from right to left
    for char in reversed(roman):
        # Get the integer value of the current Roman numeral
        value = roman_values[char]

        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            total -= value
        else:
            # Otherwise, add the value
            total += value

        # Update the previous value to the current one
        prev_value = value

    return total


# Test examples
print(roman_to_int("MM"))  # Output: 2000
print(roman_to_int("MDCLXVI"))  # Output: 1666
print(roman_to_int("M"))  # Output: 1000
print(roman_to_int("CD"))  # Output: 400
print(roman_to_int("XC"))  # Output: 90
print(roman_to_int("XL"))  # Output: 40
print(roman_to_int("I"))  # Output: 1
