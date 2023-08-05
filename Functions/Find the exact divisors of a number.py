def find_divisors(number):
    """
    Find the divisors of a given number and return them in a list.
    """
    if number == 0:
        return []

    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors

def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == "q":
            break

        try:
            number = int(user_input)
            divisors = find_divisors(number)

            if not divisors:
                print("The entered number has no divisors.")
            else:
                print("Divisors of the number:", divisors)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()
