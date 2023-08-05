# Function to calculate the area of a rectangle based on its sides' lengths
def area(demet):
    return demet[0] * demet[1]

# List of tuples representing sides' lengths of rectangles
liste = [(3, 4), (10, 3), (5, 6), (1, 9)]

# Calculate the areas of rectangles and print the results as a list
print(list(map(area, liste)))
