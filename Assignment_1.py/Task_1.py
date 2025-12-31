# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
#   o	Addition
#   o	Subtraction
#   o	Multiplication
#   o	Division
# 3.  Displays the results of each operation on the screen.


a = float(input("Enter any number:"))
b = float(input("Enter another number:"))

add = a + b
sub = a - b
mul = a * b
div = a / b

print("Addition: ", round(add))
print("Subtraction: ", round(sub))
print("Multiplication: ", round(mul))
print("Division: ", div)
