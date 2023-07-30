# Using list comprehension to create a list of even numbers from 1 to 100.

# Create a list 'liste' containing even numbers from 1 to 100 using list comprehension.
# The condition i % 2 == 0 ensures that only even numbers are included in the list.
list = [i for i in range(1, 101) if i % 2 == 0]

# Print the 'liste' containing the even numbers.
print(list)
