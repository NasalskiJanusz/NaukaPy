# collection which is ordered and unchangeable
# used to group together related data


fruits = ("apple", "banana", "cherry")
print("First thing in your stuple is: "+str(fruits[0]))
print("Lenght of your tuple is: "+str(len(fruits)))
print("Last thing in your tuple is: "+str(fruits[-1]))
print("First two thing are: " +str(fruits[0:2]))



# --------------------------------------TUPLES------------------------------------------
students = ("Kamil", "Michalak",21,"Bartek")

print(students.count("Kamil"))          #zlicza ile jest danych "Kamil" w tej liscie
print(students.index("Bartek"))         #zwraca INDEX przypisany do tej danej
for i in students:
    print(i)

if "Kamil" in students: print("Kamil tu jest!")
else: print("Nie ma go...")
