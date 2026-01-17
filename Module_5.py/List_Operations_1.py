# Slicing of lists
l1 = [1, 8, 3, 0, 4, 9, 7, 3, 6]
print(l1[1:6:1])
print(l1[2:7:2])

#  Concatenation of lists
l1 = [1, 7, 2]
l2 = [0, 5]
print(l1+l2)
print(l2+l1)

# Repetition of lists
print(l2 * 3)

# append()
#  adds an item to the end of the list
fruits = ["Mange", "Apple", "Orange"]
print(fruits)
# Syntax: list.append(item)
fruits.append("Banana")
print(fruits)
# do not use print and append fn together
# Ctrl+? gives comment

# index
# adds an element before the specified index
# syntax: list.insert(index, item)
fruits.insert(2,"Banana")
print(fruits)