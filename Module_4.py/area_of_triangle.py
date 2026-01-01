"""
This program calculates the area of a triangle using Heron's formula.

When all the three sides of the triangle is known - a, b, c
Semi perimeter (s) = (a + b + c) / 2
Area = square root of (s * (s-a) * (s-b) * (s-c))

"""

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 

print("The area of the triangle is: ", area)   