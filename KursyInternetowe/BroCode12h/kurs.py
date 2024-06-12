# --------------------------------------PODSTAWA------------------------------------------
# imie = input("Jak masz na imie?: ")
# age = int(input("Ile masz lat?: "))
# height = float(input("Ile masz wzrotstu?(cm): "))
# print("Cześć "+imie)
# if (age<=14): print("Przyjdź do mnie kiedy będziesz pełnoletnia, czyli za "+str(18 - age)+" lat/a.")
# else: print("dawaj do mnie :)))")
# if(height<179): print("Świetnie! Mój zwzrost to 179cm, czyli różni nas: "+str(179-height)+"cm.")
# elif(height>179): print("Ty jebany wysoki bambusie, wypierdalaj bo mi żyrandol potrącisz.")
# else: print("Mamy tyle samo wzrostu! 179cm :D")


#
# Text Type:	    str
# Numeric Types:	int, float, complex
#The complex() function returns a complex number by specifying a real number and an imaginary number.
#You cannot convert complex numbers into another number type.

# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType


#Losowa liczba:
# import random
# print(random.randrange(1, 10))



# ---------------------------------------LICZBY-----------------------------------------
# import math
#
# a = 1
# b = 2
# c = 3
#
# pi = 3.14
# print(round(pi))        #najbliższa liczba całkowita
# print(math.ceil(pi))    #najbliższa WYŻSZA liczba całkowita
# print(math.floor(pi))   #najbliższa NIŻSZA liczba całkowita
# print(abs(pi))          #jak daleko jest ta liczba oz 0
# print(pow(pi,2))        #podnosi liczbę o wskazaną potęgę
# print(math.sqrt(pi))    #pierwiastek z liczby
# print(max(a,b,c))       #oddaje największą liczbę
# print(min(a,b,c))       #oddaje najmniejszą liczbę


# --------------------------------------BOOL------------------------------------------

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# --------------------------------------SLICING------------------------------------------
# [start:stop:step]
# name = input("Enter your name: ")
# print("Your first letther of the name is: "+str(name[0]))
#
# wyciecie1 = name[2:5]
# wyciecie2 = name[::2]
# print("Twoje imie w zakresie znaków 2-5 to: "+wyciecie1)         #Wyświetli zakres 2-5
# print("Twoje imie używając co drugiego znaku to: "+wyciecie2)    #Wyświetli co drugi znak
# print("Twoje imie od tyłu to: "+name[::-1])                      #Wyświetli imie od tyłu
#
#                                     #funkcja slice, nadal start-stop-step
# website = "http://google.com"
# slice = slice(7,-4)
# print(website[slice])

# --------------------------------------WHILE------------------------------------------

# name = ""
# while len(name) == 0:
#     name = input("Podaj imię: ")
# print("Witaj, "+name)


# --------------------------------------FOR (odliczanie)------------------------------------------
# import time
# for i in range(10,-1,-1):
#     print(i)
#     time.sleep(1)
# print("Ale łatwo")
#                                         #LOOP W LOOPIE
# rows = int(input("How many rows? "))
# columns = int(input("How many columns? "))
# symbols = input("What kind of symbol do we want to use? ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbols, end=" ")
#     print()
# break
# while True:
#     name = input("What is your name? ")
#     if name != "":
#         break

# continue
# usuwa - z numeru telefonu używając continue do pominięcia tego znaku
# phone_number = "123-456-789-696969"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# pass - pomijanie warunkowe
#
# for i in range(1,16):
#     if i == 13: pass
#     else: print(i)



#pętla while + else
# i = 1
# while i <6:
#     print(i)
#     i += 1
# else:
#     print("Oops! i is not greather than 6 anymore!")

# --------------------------------------ARRAYS------------------------------------------

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# --------------------------------------LIST------------------------------------------
#
# food = ['apple', 'banana', 'hamburger', 'grape', 'watermelon']
#
#
# food.append('orange')                   #dodanie do listy
# food.remove("apple")                    #usuwanie z listy
# food.pop()                              #usuwa ostatnią daną z listy (ostatni index)
# food.insert(0,'cake')    #dodaje do listy w wytyczonym indexie
# food.sort()                             #sortowanie alfabetycznie
# food.clear()                            #usuwa elementy listy
#
# for foods in food:
#     print(foods)


# --------------------------------------2D-LIST------------------------------------------
#o ile pamiętam to były macierze
#
# drinks = ['coffee','milk','soda']
# desserts = ['cake','ice cream']
# dinners = ['pizza', 'hamburger', 'spaghetti']
#
# food = [drinks, desserts, dinners]
#
# print(food[0])      #wyświetli tylko listę drinks (w zależności od indeksu
# print(food[2][2])   #wyświetli tylko 3 element trzeciej listy

# --------------------------------------TUPLES------------------------------------------




# students = ("Kamil", "Michalak",21,"Bartek")
#
# print(students.count("Kamil"))          #zlicza ile jest danych "Kamil" w tej liscie
# print(students.index("Bartek"))         #zwraca INDEX przypisany do tej danej
# for i in students:
#     print(i)
#
# if "Kamil" in students: print("Kamil tu jest!")
# else: print("Nie ma go...")

# --------------------------------------SET------------------------------------------
#
#              A set is a collection which is unordered, unchangeable*, and unindexed.
#               Set items are unchangeable, but you can remove items and add new items.
#             #set jest o wiele szybszy od listy z uwagi na to, że nie jest posegregowany
#             #np. mając set z trzema danymi, po kilkukrotnym wywołanu setu zauważymi, że
#             #set wywołuje nasze dane w losowej kolejnośći
#             #JEŻELI BĘDĄ ZDUPLIKOWANE DANE TO WYŚWIETLI JĄ TYLKO RAZ NIE PATRZĄC NA TO ILE ICH TAM JEST
#
# rzeczy_kuchenne = {'nóż', 'widelec', 'łyżka'}
# naczynia = {'talerz płaski', 'talerz głęboki', 'kubek', 'nóż'}
#
# #rzeczy_kuchenne.update(naczynia)               #dodaje "naczynia" do "rzeczy_kuchenne"
# obiad = rzeczy_kuchenne.union(naczynia)         #nowa zmienna która łączy te dwa sety
# print(rzeczy_kuchenne.difference(naczynia))     #wypisuje tylko dane które się różnią między setami
# print(rzeczy_kuchenne.intersection(naczynia))   #wypisuje dane które są takie same w obu setach
# #
# # rzeczy_kuchenne.add("wazówka")
# # rzeczy_kuchenne.remove("widelec")
#
#
# for i in obiad:
#     print(i, end=", ")


# --------------------------------------DICTIONARY------------------------------------------
                    #Nie uporządkowany zbiór danych    key:value jak w bazach danych
                    #Szybkie wyjmowanie danych
                    #Można dodać/usunąć klucz i wartość w każdym momencie

# capitals = {'USA':'Washington',
#             'Russia':'Moscow',
#             'India':'Delhi',
#             'Japan':'Tokyo'}

#capitals["Poland"] = "Warsaw"

# print(capitals['Japan'])              #wywołanie klucza powoduje wypisanie wartości
# print(capitals.get('Germany'))        #sprawdzenie czy Germany jest kluczem, jeśli nie python odda "None"
# print(capitals.keys())                #wydrukuje same klucze
# print(capitals.values())              #wydrukuje same wartości
# print(capitals.items())               #drukowanie wszystkiego
# capitals.update({'Germany':'Berlin'})
# capitals.pop('India')                   #usuwanie po kluczu
# capitals.clear()                        #wyzeruje
# for key,value in capitals.items():      #drukowanie wszystkiego za pomocą pętli for
#     print(key,value)


# --------------------------------------INDEX OPERATOR[]------------------------------------------
#gives acces to sequence's element (str, list, tuples)
# name = input("Enter your name: ")
#
# # if (name[0].islower()):                   #sprawdzasz czy pierwszy element jest z małej
# #     name = name.capitalize()              #jeśli tak to zmieniasz na dużą litere
#
# first_name = name[:5].upper()               #konkretny zakres na dużą litere
# last_name = name[6:].lower()                #konkretny zakres na małą litere
# last_character = last_name[-1]              #ostatni element, przedostatni[-2] itd...
# print("Miło Cię widzieć "+first_name+" "+last_name+"!")


# --------------------------------------FUNCTIONS------------------------------------------
#część kodu która działa tylko gdy zostanie wywołana
# def siemka(first_name,second_name,age):                   #zdefiniowanie funkcji
#     print("Siemka "+first_name+" "+second_name+"!")
#     print("Masz "+age+" lat.")
# first_name= input("Enter your first name: ")
# second_name= input("Enter your second name: ")
# age = input("Enter your age: ")
# siemka(first_name,second_name,age)                        #wywołanie


# -------------------------------------RETURN STATEMENT------------------------------------------
#funkcja oddaje wartość po "przemieleniu" jej w swoim bloku kodu
#if you do not know the number of arguments that will be passed into your function,
#there is a prefix you can add in the function definition, its "*"


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

#If you do not know the number of keyword arguments that will be passed into your function,
#there is a prefix you can add in the function definition, its "**"
#
# def mnożenie(a,b):
#     return a*b
#
# print(mnożenie(2,2))
#
# liczba1 = input("Podaj pierwszą liczbe: ")
# liczba2 = input("Podaj drugą liczbe: ")
# x = mnożenie(int(liczba1),int(liczba2))
# print(x)


# -------------------------------------KEYWORD ARGUMENTS------------------------------------------
#arguments preceded by an identifier when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives
#PO PROSTU RĘCZNE PRZYPISANIE KOLEJNOŚĆI DO FUNKCJI

#       przykład

# def siemanko(a,b,c):
#     print("Siema "+ a +" "+ b +" "+ c)
# siemanko(c="słychać?",a="Janek,",b="co")
#


# -------------------------------------NESTED FUNCTIONS CALLS------------------------------------------

# nested functions calls = function calls inside other function calls
# innermost function calls are resolved first
# returned value is used as argument for the next outer function


#num = input("Enter a whole positive number: ")
#num = float (num)
#num = abs (num)
#num = round (num)
#print (num)

#print(round(abs(float(input("Enter a whole positive number: ")))))

                              #zamiast kilku linijek winięcie w jedną
                              #tak samo można zrobić z if else:
# a=3
# b=4
# print("YES") if a == b else print("NO")

# -------------------------------------SCOPE------------------------------------------
# The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created

