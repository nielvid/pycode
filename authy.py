import random

# -  Register
# _ username, email, password

# - userid  - gnerete user account
# - Login
# - (username or email), password

# bank operation


database = {}


def init():
    print('Welcome to bankPHP')
    haveAccount = int(input("Do you have account with us> 1(yes) 2(no) \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()

    else:
        print('You selected invalid option ')
        init()


def register():
    surName = input("What is your Surname \n ")
    firstName = input("What is your Firstname \n ")
    email = input("What is your email address \n ")
    username = input("Choose a username \n")
    password = input("Choose a password \n")
    accountNumber = generate_account_number()

    database[accountNumber] = {"surname": surName, "firstname": firstName, "username": username, "email": email,
                               "password": password, "accountnumber": accountNumber}
    print('Your account has been created')

    details = database[accountNumber]
    print(details)
    login()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def login():
    print("**************** LOGIN ****************")

    account_number_inputed = int(input('Enter you account number \n '))
    password = input("What is your password \n ")

    for accountNumber, items in database.items():
        print(accountNumber)
    for item in items:
        acc_no = items['accountnumber']
        dbuserpassword = items['password']
        if acc_no == account_number_inputed:
            if dbuserpassword == password:
                print('LOGIN SUCCESSFULL')
                transaction()
    print('Invalid account number or password')
    login()


def transaction():
    print('What would you like to do')
    print('Deposit')
    seletOneOption = int(input('Select 1 or 2 or 3 or 4 \n'))
    print("you seleceted %s" %seletOneOption)


# ACTUAL BANKING SYSTEM

init()
