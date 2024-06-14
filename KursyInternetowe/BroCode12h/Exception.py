# exception = events detected durign execution that interrupt
#             the flow of a program
# in other words, what program will do if we get an error that we defined

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide by: "))
# result = numerator / denominator
# print(result)

# if user will pick "0" as denominator python will return error
# basic form of handling exception is:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except Exception:
#     print("something went wrong :(")

# in this case, if user sets denominator as 0
# program won't fail, instead our string will be displayed

# REMEMBER! It's not good practise to have one except that handles all exceptions
#           It's better to make 1st specific exceptions, then the rest:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print("You can not divide by zero my friend. Go back to school.")
# except Exception:
#     print("something went wrong :(")

# now we have exception to ZeroDivisionError
# we can add as many exceptions as we possibly want
# if we delete "except Exception:" and try to divide by no number
# we will get ValueError. let's handle it.

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print("You can not divide by zero my friend. Go back to school.")
# except ValueError:
#     print("Please enter an number")
# except Exception:
#     print("something went wrong :(")

# sometimes it's better to leave rest of the exceptions
# because sometimes You can forget about any other possibilities


# we can display the exception that occurs (it's optional)
# to do this we add "as e" after our exception
# then we just print this e

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("You can not divide by zero my friend. Go back to school.")
# except ValueError as e:
#     print(e)
#     print("Please enter an number")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")


# we also can add "else" statement at the end of our exceptions
# we will print result only if there was not any errors:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can not divide by zero my friend. Go back to school.")
# except ValueError as e:
#     print(e)
#     print("Please enter an number")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)

# there is one more statement "finally"
# how it works? no matter if we catch any Errors or not,
# code after this statement will be always executed

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can not divide by zero my friend. Go back to school.")
except ValueError as e:
    print(e)
    print("Please enter an number")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute.")