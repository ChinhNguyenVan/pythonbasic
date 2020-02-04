# PRACTICE Basic Data Types, Strings and Numbers
# Types
x = 42
y = 3 / 4
z = int('7')
a = float(5)
name = "Nina"

# Numbers
rent = 480
per_day = rent / 30
print(per_day)

# Strings
print("Hello world")
name = "Nina"
print("My name is", name)

name = "Nina"
print("Hello, my name is %s" % name)

name = "Nina"
print(f"Hello, my name is {name} and I pay ${rent / 30} in rent per day")

# Helper Functions
# Python has a few built-in functions to help you if you get stuck. type() tells
# you what an object’s type is, for example a string (str) or integer (int). dir()
# returns a list of valid attributes for an object,
# so you can quickly see what variables an object has or what functions you can call on it.
# help() brings up helpful documentation on any object.
# You can also type help() on its own to bring an interactive help console.
x = 42
y = 3 / 4
name = "Nina"
type(x)
type(y)
type(name)


# PRACTICE Functions
def add_numbers1(x, y):
    return x + y


add_numbers1(2, 7)
print(f"The sum of 2 and 7 is {add_numbers1(2, 7)}")

# Function Scope

x = 1
y = 2


def add_numbers(x, y):
    print(f"Inside the function, x = {x} and y = {y}")
    return x + y


print(f"Outside the function, x = {x} and y = {y}")
print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")


# Positional Arguments vs Keyword Arguments

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y


calculate_numbers(2, 3)
calculate_numbers(2, 3, "subtract")
calculate_numbers(2, 3, operation="subtract")
