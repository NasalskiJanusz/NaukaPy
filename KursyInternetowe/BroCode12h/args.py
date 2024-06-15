# -------------------------------------*ARGS------------------------------------------


# *args = parameter that will pack all arguments into a tuple
#         useful so that a func can accept a varying amount of arguments

def add(num1, num2):
    sum = num1+num2
    return sum
print(add(1,2))

# in this case function accepts only 2 variables
# now example of using *args to make func work with any given arguments

# ! You can name *args as u want, but remember that "*" must be there
# examples: *arg, *args, *ag, *nums

def add2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add2(1,2,3,4,5,6))
# function iterates threw all args in given tuple and adds it to 'sum' then returns it
# REMEMBER - tuples are ordered and unchangeable

# if we would like to change variables in given tuple we need to make new variable that
# takes args from this tuple and changes it to, for example, list:

def add3(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 0            # we changed 1st variable to 0, then we added everything
    for i in stuff:
        sum += i
    return sum
print(add3(1,2,3,4,5,6))
