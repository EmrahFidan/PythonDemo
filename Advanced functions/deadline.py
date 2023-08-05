from datetime import datetime

def get_expiration_date():
    """
    Get the expiration date from user input.

    Returns:
        datetime: The expiration date as a datetime object.
    """
    year = int(input("Enter the expiration year: "))
    month = int(input("Enter the expiration month: "))
    day = int(input("Enter the expiration day: "))

    expiration_date = datetime(year, month, day)
    return expiration_date

def main():
    # Get the expiration date from user input
    expiration_date = get_expiration_date()

    # Get the current date and time
    current_date = datetime.now()

    # Calculate the remaining days until expiration
    remaining_days = (expiration_date - current_date).days

    print(f"{remaining_days} days remaining until the expiration date.")

if __name__ == "__main__":
    main()
