# Create an empty string to store the acrostic
acrostic = ""

# Open the file "poetry.txt" and read each line
with open("Advanced data structure and objects/poetry.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Add the first character of each line to the acrostic string
        acrostic += line[0]

# Print the acrostic
print(acrostic)
