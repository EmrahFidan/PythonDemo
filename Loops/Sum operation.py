def calculate_sum_of_numbers():
    """
    Calculates the sum of numbers entered by the user until 'q' is entered.
    """

    print("""
    Enter numbers to calculate their sum. Press 'q' to see the total.
    """)

    total = 0

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == "q":
            break

        try:
            number = int(user_input)
            total += number
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to see the total.")

    return total


if __name__ == "__main__":
    result = calculate_sum_of_numbers()
    print("The sum of the entered numbers is:", result)
