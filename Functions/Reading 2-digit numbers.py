ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def read_out_number(number):
    FIRST = number % 10
    SECOND = number // 10

    read_out = tens[SECOND] + " " + ones[FIRST]
    return read_out.strip()

def main():
    try:
        number = int(input("Enter a two-digit number: "))

        if 10 <= number < 100:
            print("Read-out:", read_out_number(number))
        else:
            print("Please enter a valid two-digit number.")
    except ValueError:
        print("Invalid input. Please enter a valid two-digit number.")

if __name__ == "__main__":
    main()
