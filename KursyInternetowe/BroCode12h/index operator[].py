# --------------------------------------INDEX OPERATOR[]------------------------------------------
#gives acces to sequence's element (str, list, tuples)
name = input("Enter your name: ")

if (name[0].islower()):                     # check if name is in lower
    name = name.capitalize()

first_name = name[:5].upper()               # specific range to make upper
last_name = name[6:].lower()                # specific range to make lower
last_character = last_name[-1]              # -1 means that we are counting from the back, -2 is second index from the end
print("Miło Cię widzieć "+first_name+" "+last_name+"!")