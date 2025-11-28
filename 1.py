# Creating a dictionary
marks = {
    'a': 10,
    'b': 25,
    'c': 55
}

# Accessing values
print("Marks of 'a':", marks['a'])
print("Marks of 'b':", marks['b'])
print("Marks of 'c':", marks['c'])

# Adding a new key-value pair
marks['d'] = 40
print("After adding 'd':", marks)

# Updating a value
marks['b'] = 30
print("After updating 'b':", marks)

# Deleting a key-value pair
del marks['a']
print("After deleting 'a':", marks)

# Looping through dictionary
print("\nAll marks:")
for key, value in marks.items():
    print(f"{key} : {value}")
