def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a  / b

2
print("""********************
CALCULATOR PROGRAM 

Operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division

********************
""")
operation = int(input("Enter the operation (1/2/3/4): "))
print("\n")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("\n")



if operation == 1:
    result = add(a, b)
    print(" {} + {} => {}".format(a, b, result))
elif operation == 2:
    result = subtract(a, b)
    print(" {} - {} => {}".format(a, b, result))
elif operation == 3:
    result = multiply(a, b)
    print(" {} * {} => {}".format(a, b, result))
elif operation == 4:
    try:
        result = divide(a, b)
        print(" {} / {} => {}".format(a, b, result))
    except ValueError as e:
        print("ERROR: {}".format(str(e)))
else:
    print("INVALID OPERATION....")
    
print("\n")
