def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            number = int(content)

        result = 100 / number
        print(f"The result of 100 / {number} is: {result}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Cannot convert the file content to an integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# example file content: "25"
file_name = "example.txt"

# Create file and write "25" in it.
with open(file_name, 'w') as file:
    file.write("25")

# Perform the transaction
process_file(file_name)

# Delete file
import os
os.remove(file_name)
