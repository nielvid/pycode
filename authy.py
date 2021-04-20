import random

# -  Register
# _ username, email, password

# - userid  - generate user account
# - Login
# - (username or email), password

# bank operation


database = {}


def deposit(amount):

    amount = amount

    print('How Much do you want to deposit')


def withdraw_cash():
    print('How Much do you want to withdraw')


def check_balance():
    balance = 500.00
    print('Your balance is %f' % balance)


def logout():
    print("You have logged out successfully")
    login()



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
                    accountbalance()
                    transaction()
    print('Invalid account number or password')
    response = input("are you sure you have account with us? YES or No \n")
    if response.lower() == 'yes':
        login()
    elif response.lower() == 'no':
        register()
    else:
        print('Invalid response')
        exit()


def accountbalance():
    username = input("Enter your username")
    for account_number, user in database.items():
        for details in user:
            owner = user['username']
            balance = user['balance']
            if owner == username:
                print('Welcome %s' % owner)
                print("your account balance is %f" % balance)
            else:
                print('Please supply username to check balance')
                transaction()

def transaction():
    print('What would you like to do')
    print('To make Deposit press 1')
    print('To make Withdrawal press 3')
    print('To logout press 4')
    print('To exit press 5')
    selected_option = int(input('Select an option \n'))
    if selected_option == 1:
       # deposit()

    elif selected_option == 2:
        #withdraw_cash()

    elif selected_option == 3:
         #check_balance()

    elif selected_option == 4:
        logout()

    elif selected_option == 5:
        exit()
    else:
        print("invalid selection, try again")
        transaction()
    print("you selected %s" % selected_option)


init()




