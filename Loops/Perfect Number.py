"""
Find the perfection of the number taken from the user.
A number is called a "perfect number" if the sum of its divisors, excluding itself, equals the number.
"""

print("""
***************
PERFECT NUMBER FINDER
***************
""")

x = int(input("Please enter a number: "))

divisor_sum = 0

# Loop through numbers from 1 to (x-1) to find the divisors of the given number x.
for i in range(1, x):
    if x % i == 0:
        divisor_sum += i

# Check if the sum of divisors equals the number itself to determine if it is a perfect number.
if x == divisor_sum:
    print("{} is a perfect number.".format(x))
else:
    print("{} is not a perfect number.".format(x))
