# Print numbers divisible by 3 between 1 and 100 using the 'continue' statement.

# Loop through numbers from 1 to 100 (inclusive).
for i in range(1, 101):
    # Check if the number is not divisible by 3.
    if i % 3 != 0:
        # If the number is not divisible by 3, skip it and continue to the next iteration.
        continue
    # If the number is divisible by 3, print it.
    print(i)
