# Create the multiplication table from 1 to 10.

# Loop through numbers from 1 to 10 (inclusive) for the first operand.
for i in range(1, 11):
    print("***************************************")
    
    # Loop through numbers from 1 to 10 (inclusive) for the second operand.
    for j in range(1, 11):
        # Calculate the product of the two operands and print the result in the format "operand1 * operand2 = product".
        print("{} * {} = {}".format(i, j, i * j))
