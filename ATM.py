class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        """Check the account balance."""
        return self.balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Invalid amount. Please deposit a positive amount."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Please enter a smaller amount."
        else:
            return "Invalid amount. Please withdraw a positive amount."

def main():
    atm = ATM()  # Create an ATM object

    print("Welcome to ATM Simulator!")
    while True:
        print("\nSelect operation:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Your balance:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using ATM Simulator!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
