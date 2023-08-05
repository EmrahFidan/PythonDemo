# Get the input string from the user
TEXT = input("Enter the sentence without spaces between words: ")

# Create an empty dictionary to store the frequency of each character
frequency = dict()

# Iterate through each character in the input string
for char in TEXT:
    # Check if the character is already in the dictionary
    if char in frequency:
        # If it is, increment its frequency by 1
        frequency[char] += 1
    else:
        # If it is not, add the character to the dictionary with a frequency of 1
        frequency[char] = 1

# Print the frequency of each character
for char, count in frequency.items():
    print(char, ":", count)
