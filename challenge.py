import textwrap


def menu():
    menu = """"\n
      ================MENU=================
      [1]\tDeposit
      [2]\tWithdraw
      [3]\tExtract
      [4]\tNew account
      [5]\tList accounts
      [6]\tNew user
      [7]\tExit
      => """
    return input(textwrap.dedent(menu))


def deposit(balance, value, extract, /):
    if value > 0:
        balance += value
        extract += f"Deposit:\tR$ {value:.2f}\n"
        print("\n===Deposit successfully!===")

    else:
        print("\n===Operation failed! The entered value is invalid.===")

    return balance, extract


def withdraw(*, balance, value, extract, limit, number_withdraws, limit_withdraws):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdraws = number_withdraws >= limit_withdraws

    if exceeded_balance:
        print("\n===Operation failed! Insufficient balance.===")

    elif exceeded_limit:
        print("\n===Operation failed! Exceeded limit.===")

    elif exceeded_withdraws:
        print("\n===Operation failed! Exceeded limit of withdrawals.===")

    elif balance > 0:
        balance -= value
        extract += f"Withdraw:\t\t {value:.2f}\n"
        number_withdraws += 1
        print("\n===Withdrawal successfully!===")

    else:
        print("\n===Operation failed! The entered value is invalid.===")

    return balance, extract


def display_extract(balance, /, *, extract):
    print("\n===========Extract===============")
    print("No moves were made." if not extract else extract)
    print("===================================")


def create_user(users):
    cpf = input("Enter your CPF (only numbers): ")
    user = filter_user(cpf, users)

    if user:
        print("\n===There is already a user with this CPF.===")
        return

    name = input("Enter your full name: ")
    age = input("Enter your age (dd-ww-yyyy): ")
    address = input(
        "Enter your address (street, number - neighborhood - city/state ): "
    )

    users.append({"name": name, "age": age, "cpf": cpf, "address": address})

    print("\n===User successfully created!===")


def filter_user(cpf, users):
    users_filtered = [user for user in users if user["cpf"] == cpf]
    return users_filtered[0] if users_filtered else None


def create_an_account(agency, account_number, users):
    cpf = input("Enter your CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("===\nAccount created successfully! ===")
        return {"agency": agency, "account_number": account_number, "user": user}

    print("\n===There is no user with this CPF.===")


def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agency:\t{account['agency']}
            C/C:\t\t{account['account_number']}
            Occount_owner:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    LIMIT_WITHDRAW = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    extract = ""
    number_withdraws = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            value = float(input("Enter the value to deposit: "))

            balance, extract = deposit(balance, value, extract)

        elif option == "2":
            value = float(input("Enter the value to withdraw: "))

            balance, extract = withdraw(
                balance=balance,
                value=value,
                extract=extract,
                limit=limit,
                number_withdraws=number_withdraws,
                limit_withdraws=LIMIT_WITHDRAW,
            )

        elif option == "3":
            display_extract(balance, extract=extract)

        elif option == "4":
            number_account = len(accounts) + 1
            account = create_an_account(AGENCY, number_account, users)

            if account:
                accounts.append(account)

        elif option == "5":
            list_accounts(accounts)

        elif option == "6":
            create_user(users)

        elif option == "7":
            print("\n===Thank you for using our services!===")
            break

        else:
            print("\n===Invalid option! Try again.===")


main()
