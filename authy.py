import random

# -  Register
# _ username, email, password

# - userid  - generate user account
# - Login
# - (username or email), password

# bank operation


database = {}


def init():
    print('Welcome to bankPHP')
    have_account = int(input("Do you have account with us> 1(yes) 2(no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()

    else:
        print('You selected invalid option ')
        init()


def register():
    surname = input("What is your Surname \n ")
    firstname = input("What is your Firstname \n ")
    email = input("What is your email address \n ")
    username = input("Choose a username \n")
    password = input("Choose a password \n")
    account_number = generate_account_number()

    database[account_number] = {"surname": surname, "firstname": firstname, "username": username, "email": email,
                                "password": password, "account_number": account_number}
    print('Your account has been created')

    details = database[account_number]
    print(details)
    login()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def login():
    print("**************** LOGIN ****************")

    account_number_input = int(input('Enter you account number \n '))
    password = input("What is your password \n ")

    for accountNumber, items in database.items():
        print(accountNumber)
    for item in items:
        acc_no = items['account_number']
        user_password = items['password']
        if acc_no == account_number_input:
            if user_password == password:
                print('LOGIN SUCCESSFUL')
                transaction()
    print('Invalid account number or password')
    login()


def transaction():
    print('What would you like to do')
    print('To make Deposit press 1')
    print('To make Withdrawal press 3')
    print('To exit press 4')
    selected_option = int(input('Select an option \n'))
    if selected_option == 1:
        def deposit():
            pass
    elif selected_option == 2:
        def withdraw_cash():
            pass
    elif selected_option == 3:
        def check_balance():
            pass
    print("you selected %s" % selected_option)


# ACTUAL BANKING SYSTEM

init()
