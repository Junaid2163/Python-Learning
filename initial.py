# Creating a tuple
fruits = ("apple", "banana", "cherry", "mango")

# Printing the tuple
print("Tuple:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing a tuple
print("First two fruits:", fruits[:2])

# Counting occurrences
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Number of times 2 appears:", numbers.count(2))

# Finding the index of an element
print("Index of cherry:", fruits.index("cherry"))

# Iterating through a tuple
print("Fruits in the tuple:")
for fruit in fruits:
    print(fruit)

# Tuple packing
person = ("Alice", 25, "Engineer")

# Tuple unpacking
name, age, profession = person

print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)
