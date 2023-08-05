def fibonacci():
    # Initialize the first two Fibonacci numbers
    a, b = 1, 1

    # Yield the first two numbers
    yield a
    yield b

    while True:
        # Generate the next Fibonacci number and swap variables for the next iteration
        a, b = b, a + b
        yield b

def print_fibonacci_numbers(limit):
    for i in fibonacci():
        # Break the loop if the Fibonacci number exceeds the given limit
        if i > limit:
            break
        else:
            # Print the Fibonacci number
            print(i)

if __name__ == "__main__":
    # Print Fibonacci numbers up to a limit of 100,000
    print_fibonacci_numbers(100000)
