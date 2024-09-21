import random

class ATM:
    def _init_(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def check_balance(self):
        print(f"\n{self.account_holder}, your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")

    def check_account_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")

    def exit(self):
        print(f"Thank you for using the ATM, {self.account_holder}. Goodbye!")


def atm_menu(account_holder):
    atm = ATM(account_holder, balance=1000)  # Initial balance set to $1000
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Details")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the deposit amount: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '4':
            atm.check_account_details()
        elif choice == '5':
            atm.exit()
            break
        else:
            print("Invalid choice! Please try again.")


def insert_atm_card():
    print("🏦 CeedoTech ATM Machine 🏧")
    name = input("Please insert your ATM card or alternatively input your name: ")
    
    while not name.strip():  # Ensuring that the user enters a valid name
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Please input your name: ")
    
    return name.strip()

if __name__ == "__main__":
    account_holder = insert_atm_card()
    atm_menu(account_holder)
