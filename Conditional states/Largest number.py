def find_maximum_number():
    # Get three input numbers from the user
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))

    # Find the maximum of the three numbers using the built-in max function
    maximum = max(num1, num2, num3)

    # Print the largest number
    print("The largest number is: {}".format(maximum))

if __name__ == "__main__":
    # Call the find_maximum_number function when this script is run
    find_maximum_number()
