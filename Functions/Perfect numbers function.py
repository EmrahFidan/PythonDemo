def is_perfect_number(number):
    """
    Check if a given number is a perfect number.
    A number is perfect if the sum of its divisors (excluding itself) is equal to the number itself.
    """
    total_divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            total_divisors_sum += i
    return total_divisors_sum == number

def find_perfect_numbers(limit=1000):
    """
    Find perfect numbers from 1 up to the given limit (default: 1000).
    """
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

def main():
    perfect_numbers = find_perfect_numbers()

    for number in perfect_numbers:
        print("Mükemmel Sayı:", number)

if __name__ == "__main__":
    main()
