def gcd(number1, number2):
    """
    Find the greatest common divisor (GCD) of two given numbers.
    """
    while number2 != 0:
        number1, number2 = number2, number1 % number2

    return number1

def main():
    number1 = int(input("Number-1: "))
    number2 = int(input("Number-2: "))

    print("EBOB:", gcd(number1, number2))

if __name__ == "__main__":
    main()
