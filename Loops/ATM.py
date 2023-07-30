import argparse

def display_menu():
    # Display the main menu for the ATM machine.
    print("""
**************
Welcome to the ATM machine

Transactions:
1. Check Balance
2. Deposit Money
3. Withdraw Money

Press 'q' to exit.
**************
""")

def check_balance(balance):
    # Function to check and display the account balance.
    print("Your balance is {} TL.".format(balance))

def deposit_money(balance):
    # Function to deposit money into the account.
    amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print("Your new balance is {} TL.".format(balance))
    return balance

def withdraw_money(balance):
    # Function to withdraw money from the account.
    amount = int(input("Enter the amount to withdraw: "))
    if balance - amount < 0:
        print("You don't have enough balance.")
        return balance
    balance -= amount
    print("Your new balance is {} TL.".format(balance))
    return balance

def main():
    # Parse the command-line arguments to get the initial balance.
    parser = argparse.ArgumentParser(description="ATM machine")
    parser.add_argument("--balance", type=int, default=3000, help="Initial account balance")
    args = parser.parse_args()
    balance = args.balance

    while True:
        # Display the main menu and prompt user for the transaction choice.
        display_menu()
        transaction = input("Choose your transaction: ")

        if transaction == "q":
            # Exit the ATM if the user chooses to quit.
            print("Thank you for using our ATM. Have a nice day!")
            break
        elif transaction == "1":
            # Perform the "Check Balance" transaction.
            check_balance(balance)
        elif transaction == "2":
            # Perform the "Deposit Money" transaction.
            balance = deposit_money(balance)
        elif transaction == "3":
            # Perform the "Withdraw Money" transaction.
            balance = withdraw_money(balance)
        else:
            # Invalid transaction choice.
            print("Invalid transaction")

if __name__ == "__main__":
    # Run the main function when the script is executed.
    main()
