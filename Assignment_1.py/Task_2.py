# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
#  1.  Takes a user's first name and last name as input.
#  2.  Concatenates the first name and last name into a full name.
#  3.  Prints a personalized greeting message using the full name.


fn = str(input("Enter your first name: "))
ln = str(input("Enter your last name: "))

# Concatenate the names to create the full name
# We add a space " " between the first and last name
full_name = fn+ " " + ln

# 3. Print the personalized greeting
# Using an f-string for clean formatting
print(f"Hello, {full_name}! Welcome to the Python program.")