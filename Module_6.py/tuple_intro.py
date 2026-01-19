# Tuple
# (item 1, item 2, item 3,.... ) OR without any brackets bydefault is tuple
# Sequence of items as a collection
# This is not mutable(no changes can be made)

t1 = ("Python", 10, 1.5, True, [1, 2, 4], (10, 20))
print(len(t1))

# Accessing items of a tuple - index
print(t1[0])
print(t1[-1])

l1 = [1, 2, 3]
print(l1, type(l1))
t1 = tuple(l1)
print(t1, type(t1))
print(l1, type(l1))
# Type casting does not make changes to the existing data

fruits = ("Mango", "Orange", "Apple")
print(fruits, type(fruits))
frits = list(fruits)
print(fruits, type(fruits))
