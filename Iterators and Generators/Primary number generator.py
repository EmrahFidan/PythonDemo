def is_prime(number):
    """
    Check if the given number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    # Check for factors up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def prime_generator():
    """
    Generator function to yield prime numbers.

    Yields:
        int: The next prime number.
    """
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1


if __name__ == "__main__":
    # Print prime numbers up to 1000
    for number in prime_generator():
        if number > 1000:
            break
        print(number)
