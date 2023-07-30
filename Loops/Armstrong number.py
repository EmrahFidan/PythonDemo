def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0

    # Calculate the sum of each digit raised to the power of num_digits
    for digit_str in num_str:
        digit = int(digit_str)
        total += digit ** num_digits

    return total == number


try:
    input_number = int(input("Number:"))

    if is_armstrong_number(input_number):
        print(input_number, "is an Armstrong number.")
    else:
        print(input_number, "is not an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter a number.")
