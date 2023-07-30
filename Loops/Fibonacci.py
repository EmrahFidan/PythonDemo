def generate_fibonacci_series(n):
    """
    Generates a Fibonacci series of length n and returns it as a list.
    Fibonacci Series is created by adding the previous two numbers to get the next number.
    For example: 1, 1, 2, 3, 5, 8, 13, 21, 34...
    """
    if n <= 0:
        raise ValueError("The length of the series should be a positive integer.")

    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fibonacci_series = [1, 1]  # Initialize the series with the first two elements: 1, 1

    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]  # Calculate the next number in the series
        fibonacci_series.append(next_number)  # Add the next number to the series

    return fibonacci_series


if __name__ == "__main__":
    try:
        length = int(input("Enter the number of elements for the Fibonacci series: "))  # Get user input for the length of the series
        result = generate_fibonacci_series(length)  # Generate the Fibonacci series
        print(result)  # Print the resulting Fibonacci series
    except ValueError as e:
        print(f"Error: {e}")  # Handle the case when the user provides a non-integer input for the length
