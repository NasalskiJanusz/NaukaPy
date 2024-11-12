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


# iterating by index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])