import random

database = {8692483462: {"surname": "Jide", "firstname": "Tayo", "username": "jide1", "email": "jide@gmail.com",
                         "password": 123456, "account_number": 8692483462, "balance": 500.00}}


def init():
    print('Welcome to bankPHP')
    try:
        have_account = int(input("Do you have account with us> 1(yes) 2(no) \n"))
        if have_account == 1:
            login()
        elif have_account == 2:
            register()

        else:
            print('You selected invalid option ')
            init()
    except ValueError as ve:
        print(ve)


def register():
    surname = input("What is your Surname \n ")
    firstname = input("What is your Firstname \n ")
    email = input("What is your email address \n ")
    username = input("Choose a username \n")
    password = input("Choose a password \n")
    account_number = generate_account_number()
    balance = 0.00

    database[account_number] = {"surname": surname, "firstname": firstname, "username": username, "email": email,
                                "password": password, "account_number": account_number, "balance": balance}
    print('Your account has been created')

    print(database)
    login()


def login():
    print("**************** LOGIN ****************")

    account_number_input = int(input('Enter you account number \n '))
    password = input("What is your password \n ")

    user = loop_tru_database(account_number_input)

    acc_no = user['account_number']
    user_password = user['password']
    if acc_no == account_number_input:
        if user_password == password:
            print('LOGIN SUCCESSFUL')
            transaction()
    else:
        print('Invalid account number or password')
    response = input("are you sure you have account with us? YES or No \n")
    if response.lower() == 'yes':
        login()
    elif response.lower() == 'no':
        register()
    else:
        print('Invalid response')
        exit()


def transaction():
    print('What would you like to do')
    print('To make Deposit press 1')
    print('To make Withdrawal press 3')
    print('To logout press 4')
    print('To exit press 5')
    selected_option = int(input('Select an option \n'))
    if selected_option == 1:
        deposit(200)

    elif selected_option == 2:
        withdraw_cash()

    elif selected_option == 3:
        check_balance()

    elif selected_option == 4:
        logout()

    elif selected_option == 5:
        exit()
    else:
        print("invalid selection, try again")
        transaction()
    print("you selected %s" % selected_option)


def logout():
    print("You have logged out successfully")
    login()


def loop_tru_database(acc):
    try:
        if acc in database:
            user = database[acc]
            return user
        else:
            raise LookupError
    except LookupError:
        print("Account Number does not exist in our bank")


def ask_todo_something_else():
    response = input("Would you like to do something else? \n")
    if response.lower() == 'yes':
        login()
        transaction()
    elif response.lower() == 'no':
        exit()
    else:
        print('Invalid response')
        exit()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def deposit(amount):
    amount = amount
    print('You deposited %d' % amount)
    ask_todo_something_else()


def withdraw_cash():
    print('How Much do you want to withdraw')


def check_balance():
    balance = 500.00
    print('Your balance is %f' % balance)


def account_balance():
    account_number = int(input("Enter your username \n"))
    user = loop_tru_database(account_number)
    owner = user['account_number']
    balance = user['balance']
    if owner == account_number:
        print("Your account balance is: %f" % balance)
        transaction()
    else:
        print('Wrong Account Number supplied')
        account_balance()