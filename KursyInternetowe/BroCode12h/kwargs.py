# --------------------------------------**KWARGS-----------------------------------------
# key word arguments

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keywords args
#            also, you dont need to call them "**kwargs", all matters are those two "**"

# def hello(firs, last):
#     print("Hello " + firs + " " + last)
#
# hello(first ="John",middle = "Arthur",last ="Doe")

# this func accepts only 2 arguments and displays it.
# but what when somebody has 2 names like in this case? use **kwargs

# def hello2(**kwargs):
#     print("Hello, " + kwargs["first"] + " " + kwargs["middle"] + " " + kwargs["last"])

# as you can see we need to define which arg we want to use
# kwarg["arg we want to use"]
# we also can iterate through given kwargs:

# def hello3(**kwargs):
#     print("Hello ")
#     for key, value in kwargs.items():
#         print(value)

# now it prints every value in new line
# we can change it by adding end statement:

# def hello4(**kwargs):
#     print("Hello",end=" ")
#     for key, value in kwargs.items():
#         print(value,end=" ")

# now it prints everything in the same line
# and also we can give any amount of arguments as we want

# hello4(first="John",middle="Arthur",last="Doe")