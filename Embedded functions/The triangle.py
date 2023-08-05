# Function to check if a tuple represents a valid triangle based on its side lengths
def is_triangle(triple):
    if (abs(triple[0] + triple[1]) > triple[2] and abs(triple[0] + triple[2]) > triple[1] and abs(triple[1] + triple[2]) > triple[0]):
        return True
    else:
        return False

# List of tuples representing sides' lengths of triangles
triangle_list = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]

# Filter the list to keep only the tuples representing valid triangles and print the result
print(list(filter(is_triangle, triangle_list)))
