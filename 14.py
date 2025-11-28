# Create a tuple
my_tuple = (10, 20, 30)

# 1) Add items (tuples are immutable → create a new one)
new_tuple = my_tuple + (40, 50)
print("New tuple:", new_tuple)

# 2) len()
print("Length:", len(new_tuple))

# 3) Check for item in tuple
print("Is 20 in tuple?", 20 in new_tuple)

# 4) Access items
print("First item:", new_tuple[0])
print("Last item:", new_tuple[-1])
