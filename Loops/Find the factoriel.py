def calculate_factorial(n):
    """
    Calculates the factorial of a given non-negative integer n and returns the result.
    Factorial of a non-negative integer n is the product of all positive integers up to n.
    For example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n < 0:
        raise ValueError("Factorial is defined for non-negative integers only.")

    factorial = 1  # Initialize the factorial variable to 1
    for num in range(2, n + 1):  # Loop through the range from 2 to n (inclusive)
        factorial *= num  # Multiply each number in the range to the current factorial value

    return factorial  # Return the calculated factorial


if __name__ == "__main__":
    print("****************************")
    print("Factorial Calculation Program")
    print('Enter "q" to exit.')
    print("****************************")

    while True:  # Infinite loop to keep the program running until user chooses to exit
        user_input = input("Enter a number to calculate its factorial: ")  # Get user input for the number or 'q' to quit

        if user_input.lower() == "q":  # If the user enters 'q', exit the loop and the program
            print("Exiting the program...")
            break

        try:
            number = int(user_input)  # Convert the user input to an integer
            if number < 0:  # Check if the number is negative
                print("Factorial is not defined for negative numbers.")
            else:
                result = calculate_factorial(number)  # Calculate the factorial of the number
                print("{}! = {}".format(number, result))  # Print the result in the format "number! = result"
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.")  # Handle invalid inputs with an error message
