import time

# data base
users = {1: ["Jan", "Kowalski", 1],
         2: ["Antek", "Tkacz", 2],
         3: ["Kasia", "Żbik", 3],
         4: ["Ada", "Chrust", 4],
         6: ["Tomasz", "Berbeć", 5],
         7: ["Janusz", "Michnik", 6]}
# temp admin password
admin_password = "j"


# "clear" console
def clear_console():
    print("\n" * 10)


# check user input
def user_input():
    n = input("\nEnter your name: ").lower().capitalize()
    s = input("Enter your surname: ").lower().capitalize()
    p = input("Enter your service id: ")
    while True:
        # if user tried to set name as number or left empty field
        if n.isdigit() is True or n == "":
            print("\nName field can not be empty or number.")
            n = input("\nCorrect your name: ").lower().capitalize()
        # if user tried to set surname as number or left empty field
        elif s.isdigit() is True or s == "":
            print("\nSurname field can not be empty or be a number.")
            s = input("Correct your surname: ").lower().capitalize()
        # if user tried to set ID using letters or left empty field
        elif p.isdigit() is not True or p == "":
            print("\nID field can not be empty or have any letters.")
            p = input("Correct your service ID: \n")
        # if inputs are valid
        else:
            # if user input makes sense - ask user if he changed mind
            sense = input("\nYou are about to add new user, did you change your mind?\n1. No\n2. Yes\nYour choice: ")

            # exits to main menu
            if sense == "2":
                pass
            # execute function that adds user
            elif sense == "1":
                add_user(n, s, p)
                break
    return n, s, p


def add_user(n, s, p):
    lista = list(users.keys())
    for key in users:

        # if user already exist
        if users[key][2] == int(p):
            return print("User already exists.")
        # check if any id in between of others is free
        elif sum(users) != sum(range(1, len(users) + 1)):
            # check if IDs are correct
            lista = list(users.keys())
            missing = -1
            for i in lista:
                # real result
                #print("Lista [i+1]: ", lista[i + 1])
                # what it should be
                #print("Lista[1]+1", lista[i] + 1)
                if lista[i]+1 != lista[i+1]:
                    missing = min(lista[i]+1,lista[i+1])
                    print(min(lista[i]+1,lista[i+1]))

            break
        # if we checked all users and found no matches is IDs
        elif users[key] == users[str(len(users))]:
            # add new id key in DB and set values to it
            users[str(len(users) + 1)] = [str(n), str(s), int(p)]
            return print(
                "\nNew user: " + str(n) + " " + str(s) + " associated with ID: " + str(p) + " added successfully.")
        # check next user ID
        else:
            continue

# dunction to del user
def del_user(a):
    for key in users:
        # ask administartor if he really wants to remove user
        choice = input("\nYou are about to delete column in DB, are you sure?"
                       "\n1. Yes\n2. No\nYour choice: ")
        # if yes remove
        if choice == "1" and users[key][2] == int(a):
            users.pop(str(a))
            return print("User deleted.")
        elif choice == "2":
            return print("You changed your mind. User is still in DB.")
        else:
            pass



# whole program to work on DB
while True:
    lista = list(users.keys())
    print("Lista: ",lista)

    # print(lista[0]+1)
    for i in range(len(lista)):
        print(lista[i + 1] - 1)
        #print("I: "+str(i)+" Lista[i]: "+str(lista[i]))
        # if Lista[0] == 1 != lista[
        # aktualne     następny index
        #if lista[i] != lista[i+1]-1:
        #     print("Lista[i] - id: "+ str(lista[i])+" lista[i]+1 - value: "+ str(lista[i]+1))
        # print(str(i)+". i[i]+1: "+str(lista[i] + 1))
        # print(str(i)+".[i+1]: "+ str(lista[i+1]))
    # menu

    print("What do you want to do?\n1. Add user\n2. Remove user\n3. Update user\n4. Exit\n")
    user_action = input("Enter your choice: ")

    # check if choose is valid
    if user_action not in ("1", "2", "3", "4"):
        clear_console()
        print("\nInvalid input, please choose correct number from 1 to 4.\n")
        continue
    else:
         choose = user_action

    # adding user
    if choose == "1":
        clear_console()
        # this function checks users input and if everything is correct adds it to the DB
        user_input()
        # if user was added
        while True:
            # add one more or go back to main menu
            question = input("\n\nWhat do you want to do now?\n1. Add one more user\n2. Go back to main menu\n\nYour choice: ")
            # invalid choose
            if question not in ("1", "2"):
                print("\nInvalid input, please choose correct number.\n")
                continue
            # add one more user
            elif question == "1":
                user_input()
                break
            # go back to main menu
            elif question == "2":
                break
    # remove user
    elif choose == "2":
        print("To delete user please enter password: \n")
        inputPassword = input("Enter your password: ")
        # if password is not valid
        if inputPassword != admin_password:
            print("Administrator password does not match with your password.")
        # valid password
        else:
            clear_console()
            print("Password valid. Which user do you want to remove?"
                  "\nTo point at him select his Number ID from below:\n")
            # print users 1 by 1 (should be easy to read)
            for i in users:
                print("Number ID: {:10} Name: {:10} Surname: {:10} Service ID: {:<10}".format(
                    str(i), str(users[i][0]), str(users[i][1]), users[i][2]), end="\n")
                time.sleep(0.2)

            # choose user to remove
            while True:
                deus = input("\nYour choice: ")
                if int(deus) in range(len(users))[1:] and str(deus) != "":
                    del_user(str(deus))
                    break
                else:
                    continue
