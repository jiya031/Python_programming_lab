# Create a list with numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate odd and even
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print lists
print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)

# Print counts
print("Count of Odd Numbers:", len(odd_numbers))
print("Count of Even Numbers:", len(even_numbers))
