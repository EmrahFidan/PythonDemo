def is_prime(number):
    """
    Check if a given number is a prime number.
    """
    if number == 1:
        return False

    if number == 2:
        return True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == "q":
            break

        try:
            number = int(user_input)
            if is_prime(number):
                print(number, "is a prime number.")
            else:
                print(number, "is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()
