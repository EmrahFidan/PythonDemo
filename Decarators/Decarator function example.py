def ekstra(func):
    def wrapper(numbers):
        even_avg, odd_avg = calculate_odd_even_averages(numbers)
        print("Average of odd numbers:", odd_avg)
        print("Average of even numbers:", even_avg)

        func(numbers)

    return wrapper


def calculate_average_numbers(numbers):
    # Calculate the sum of numbers and the count of numbers
    total_sum = 0
    count = 0

    for number in numbers:
        total_sum += number
        count += 1

    return total_sum / count


def calculate_odd_even_averages(numbers):
    # Calculate the sum and count of odd and even numbers separately
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
            even_count += 1
        else:
            odd_sum += number
            odd_count += 1

    return even_sum / even_count, odd_sum / odd_count


@ekstra
def calculate_overall_average(numbers):
    # Calculate the overall average of the numbers
    overall_avg = calculate_average_numbers(numbers)
    print("Overall Average:", overall_avg)


calculate_overall_average([1, 2, 3, 4, 34, 60, 63, 32, 100, 105])
