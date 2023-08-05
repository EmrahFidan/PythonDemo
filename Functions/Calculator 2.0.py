import math

# Constants
EXIT_OPTION = "q"

# Functions for each operation
def add_numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("RESULT = ", a + b)

def subtract_numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("RESULT = ", a - b)

def multiply_numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("RESULT = ", a * b)

def divide_numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if b == 0:
        print("ERROR: Cannot divide by zero.")
    else:
        print("RESULT = ", a / b)

def round_up():
    a = float(input("Enter a decimal number: "))
    print("RESULT = ", math.ceil(a))

def find_gcd():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("RESULT = ", math.gcd(a, b))

def find_absolute_value():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.fabs(a))

def calculate_factorial():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.factorial(a))

def round_down():
    a = float(input("Enter a decimal number: "))
    print("RESULT = ", math.floor(a))

def find_remainder():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("RESULT = ", math.fmod(a, b))

def calculate_area_of_circle():
    radius = int(input("Enter the radius: "))
    print("RESULT = ", (radius * radius) * math.pi)

def calculate_circumference_of_circle():
    radius = int(input("Enter the radius: "))
    print("RESULT = ", radius * math.tau)

def calculate_log_base_2():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.log2(a))

def calculate_log_base_10():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.log10(a))

def calculate_power():
    a = int(input("Enter a number: "))
    b = int(input("Enter the power: "))
    print("RESULT = ", math.pow(a, b))

def calculate_square_root():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.sqrt(a))

def convert_degree_to_radian():
    a = int(input("Enter a number in degrees: "))
    print("RESULT = ", math.radians(a))

def calculate_sine():
    a = int(input("Enter a number: "))
    print("RESULT = ", math.sin(a))

# Display menu
def display_menu():
    print("""
    1. Sum
    2. Subtraction
    3. Multiplication
    4. Division
    5. Round up to the nearest integer
    6. Greatest Common Divisor (EBOB)
    7. Absolute Value
    8. Factorial
    9. Round down to the nearest integer
    10. Remainder
    11. Area of Circle
    12. Circumference of Circle
    13. Logarithm Base 2
    14. Logarithm Base 10
    15. Power
    16. Square Root
    17. Convert Degree to Radian
    18. Calculate Sine
    19. Exit
    """)

# Main program
def main():
    print("Welcome to Math Calculator 2.0!")

    while True:
        display_menu()
        operation = input("Enter the operation number you want to use (or 'q' to quit): ")

        if operation == EXIT_OPTION:
            print("CHECKING OUT...")
            break

        if not operation.isdigit():
            print("ERROR: Invalid input. Please enter a valid number.")
            continue

        operation = int(operation)

        if 1 <= operation <= 19:
            # Call the corresponding operation function based on the user's choice
            operations = [
                add_numbers,
                subtract_numbers,
                multiply_numbers,
                divide_numbers,
                round_up,
                find_gcd,
                find_absolute_value,
                calculate_factorial,
                round_down,
                find_remainder,
                calculate_area_of_circle,
                calculate_circumference_of_circle,
                calculate_log_base_2,
                calculate_log_base_10,
                calculate_power,
                calculate_square_root,
                convert_degree_to_radian,
                calculate_sine,
            ]
            operations[operation - 1]()  # Execute the selected operation
        else:
            print("ERROR: Invalid operation number. Please choose a valid operation.")

if __name__ == "__main__":
    main()
