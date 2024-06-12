txt = " Hello world "
txt.split
print(txt.strip())                          #usuwa spacje
txt = "Hello world"
print(txt[2:5])                             #wypisuje 2:5 "llo"
print(txt.upper())                          #uppercase
print(txt.lower())                          #lowercase
print(txt.replace("H","J"))     #zamiana znaków


'''
Method	            Description

capitalize()    	Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found

isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()     	Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case

join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
'''



#Adding placeholder
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Create an f-string:                  combine strings and numbers by using f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals:
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# A placeholder can contain Python code, like math operations:
# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)


