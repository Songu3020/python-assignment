def log_application():
    balance = 0.0
    show_transaction = []

    while True:
        print("""
WHAT IS HAPPENING TODAY?
1. Deposit money
2. Withdraw money
3. Show transaction history
4. Exit the program
""")

        try:
            log = int(input("What is happening today? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if log == 1:
            amount = float(input("How much do you want to deposit? "))
            balance += amount
            record = f"You deposited {amount:.2f}, balance is {balance:.2f}"
            show_transaction.append(record)
            print(record)

        elif log == 2:
            withdraw = float(input("How much do you want to withdraw? "))
            if withdraw > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw
                record = f"You withdrew {withdraw:.2f}, balance is {balance:.2f}"
                show_transaction.append(record)
                print(record)

        elif log == 3:
            if not show_transaction:
                print("No transactions yet")
            else:
                for i, t in enumerate(show_transaction, 1):
                    print(f"{i}. {t}")

        elif log == 4:
            print(f"Final balance: {balance:.2f}")
            print("THANK YOU FOR USING TRANSACTION LOG APP")
            break

        else:
            print("Invalid option")
            

log_application()

