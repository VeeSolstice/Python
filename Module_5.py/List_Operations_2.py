"""
extend()
remove()
pop()    
"""

# extend
fruits = ["Apple", "Mango", "Orange"]
# fruits.append("Banana", "Grapes")
# This above sntax throws an error because append fn can add only one element at a time not more
# print(fruits)

# fruits.append(["Banana", "Grapes"])
# This will not throw an error because it considers everything inside the bracket as one. 
# So, it will display list with one more list inside it
# print(fruits)

# fruits.extend("Banana" ,"Grapes")
# This also gives TypeError
# print(fruits)

fruits.extend(["Banana","Grapes"])
print(fruits)



# Remove
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.remove("Mango")
print(fruits)
fruits = ["Apple", "Mango", "Orange", "Mango"]
fruits.remove("Mango")
# This fn removes first occurance incase of multiple occurances

# fruits.remove("Banana")
# This throws ValueError



# pop
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.pop(2)
print(fruits)

fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.pop()
# This bydefault removes the last element
print(fruits)