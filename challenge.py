menu = """"

  [1] - Register
  [2] - Withdraw
  [3] - Statement
  [4] - Exit

=> """

balance = 0
limit = 500
statiment = ""
number_withdraws = 0
LIMIT_WITHDRAW = 3

while True:
    option = input(menu)

    if option == "1":
        value = float(input("Enter the value to deposit: "))

        if value > 0:
            balance += value
            statiment += f"Deposit: R$ {value:.2f}\n"

        else:
            print("Invalid value!")

    elif option == "2":
        value = float(input("Enter the value to withdraw: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdraws = number_withdraws >= LIMIT_WITHDRAW

        if exceeded_balance:
            print("Operation failed! Insufficient funds!")

        elif exceeded_limit:
            print("Operation failed! Value exceeded the limit!")

        elif exceeded_withdraws:
            print("Operation failed! Exceeded number of withdrawals!")

        elif value > 0:
            balance -= value
            statiment += f"Withdraw: R$ {value:.2f}\n"
            number_withdraws += 1

        else:
            print("Operation failed! Invalid value!")

    elif option == "3":
        print("\n================STATIMENT================\n")
        print("No move was made!" if not statiment else statiment)
        print(f"\nBalance: R$ {balance:.2f}")
        print("\n=========================================\n")

    elif option == "4":
        print("Thank you for using our services!")
        break

    else:
        print("Invalid option! Please, re-select the desired operation!")
