# --------------------------------------FUNCTIONS------------------------------------------
def siemka():
    first_name = input("Enter your first name: ")
    second_name = input("Enter your second name: ")
    age = input("Enter your age: ")
    print("Hi "+first_name.capitalize()+" "+second_name.capitalize()+"!")
    print("You are "+age+" years old.\n")
# calling function:
# siemka()


# nice way to use function:
def is_even(x):
    return x % 2 == 0
my_list = [1,2,3,4,5,6,7,8,9]
# just use filter method
# this method is used to process a sequence (list, tuple, etc.)
# it returns elements that satisfy specific conditions
# it takes two arguments:
# (Function that returns True or False and Sequence of elements)

result = filter(is_even, my_list)
print(list(result))
