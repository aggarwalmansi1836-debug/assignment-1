# Initial details
balance = 5000
correct_pin = "1234"

# Function to check balance
def check_balance():
    print("Current Balance: ₹", balance)

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print("₹", amount, "deposited successfully.")
    print("New Balance: ₹", balance)

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
        print("Remaining Balance: ₹", balance)
    else:
        print("Insufficient Balance!")

# Login
pin = input("Enter your ATM PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid Choice! Please try again.")

else:
    print("Incorrect PIN! Access Denied.")