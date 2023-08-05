# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to calculate the sum of two numbers
def add_numbers(x, y):
    return x + y

from functools import reduce

# Original list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter the list to keep only the even numbers
even_numbers_list = list(filter(is_even, numbers_list))

# Calculate the sum of even numbers using the reduce function
result = reduce(add_numbers, even_numbers_list)

print("Sum of even numbers:", result)
