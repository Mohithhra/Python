print("Welcome to Simple ATM Simulator")
print("-------------------------------")

balance = 5000
pin = "1234"

user_pin = input("Enter your PIN: ")

if user_pin == pin:
    print("PIN Verified Successfully")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your Current Balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Amount Deposited Successfully")
            print("Updated Balance:", balance)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance")

        elif choice == "4":
            print("Thank you for using ATM Simulator")
            break

        else:
            print("Invalid Choice! Please try again")

else:
    print("Wrong PIN! Access Denied")
