"""
reverse()
sort()
count()
Membership Operation
"""
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
print(days_of_week)

# reverse()
days_of_week.reverse()
print(days_of_week)

# sort()
nums = [4, 9, 0, 1, 2, 8]
# Ascending order
nums.sort()
print("Sorted List:", nums)

# Descending order
nums.sort(reverse = True)
print("Sorted List:", nums)

# count()
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
c = numbers.count(item_to_count)
print(f"Occurence of {item_to_count} is {c}")

# in()
language = ["Pyhton", "Java", "C++", "Python"]
print("Python" in language)
print("Javascript" in language)

# not in
language = ["Pyhton", "Java", "C++", "Python"]
print("Python" not in language)
print("Javascript" not in language)