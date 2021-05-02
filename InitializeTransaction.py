import random
from Validation import validate_input_as_number, validate_to_tendigits
from Queries import create_account, read_from_database, get_acc_details_from_database, update_account


def init():
    print('Welcome to bankPHP')
    try:
        have_account = validate_input_as_number(input("Do you have account with us> 1(yes) 2(no) \n"))
        if have_account == 1:
            login()
        elif have_account == 2:
            register()
        else:
            print('You selected invalid option')
            init()
    except ValueError:
        print("Something is wrong with your input")
        init()


def register():
    try:
        surname = input("What is your Surname \n ")
        firstname = input("What is your Firstname \n ")
        email = input("What is your email address \n ")
        username = input("Choose a username \n")
        password = input("Choose a password \n")
        account_number = generate_account_number()
        balance = 0.00

        account_number = {"surname": surname, "firstname": firstname, "username": username, "email": email,
                          "password": password, "account_number": account_number, "balance":  balance}
        account_id = account_number["account_number"]
        create_account(account_id, account_number)
        print('Your account was created successfully')
        user = read_from_database(account_id)
        new_acc_number = user["account_number"]
        print("Your account Number is %d" % new_acc_number)
        login()
    except Exception as e:
        print("Error creating your account", e.__class__)


def login():
    try:
        print("*******LOGIN TO MAKE TRANSACTIONS ****************")

        account_number_input = validate_to_tendigits(input('Enter you account number \n '))
        if not account_number_input:
            login()
        account_number_input = validate_input_as_number(account_number_input)
        password = input("What is your password \n ")

        # user = loop_tru_database(account_number_input)
        user = get_acc_details_from_database(account_number_input)
        acc_no = user['account_number']
        user_password = user['password']
        if acc_no == account_number_input:
            if user_password == password:
                print('LOGIN SUCCESSFUL')
                transaction(acc_no)
            else:
                response = input("are you sure you have account with us? YES or No \n")
                if response.lower() == 'yes':
                    login()
                elif response.lower() == 'no':
                    register()
                else:
                    print('Invalid response')
                    exit()
        else:
            print('Invalid account number')
            login()

    except Exception as e:
        print('Something went wrong', e.__class__)


def transaction(acc_no):
    try:
        print('What would you like to do')
        print('To make Deposit press 1')
        print('To make Withdrawal press 2')
        print('To check Balance press 3')
        print('To transfer cash press 4')
        print('To logout press 5')
        print('To exit press 6')
        selected_option = int(input('Select an option \n'))
        if selected_option == 1:
            deposit(acc_no)

        elif selected_option == 2:
            withdraw_cash(acc_no)

        elif selected_option == 3:
            get_balance(acc_no)

        elif selected_option == 4:
            transfer_cash(acc_no)

        elif selected_option == 5:
            logout()

        elif selected_option == 6:
            print("Goodbye")
            exit()
        else:
            print("invalid selection, try again")
            transaction(acc_no)
        ask_todo_something_else()
    except Exception as e:
        print("Something went wrong", e.__class__)


def logout():
    print("You have logged out successfully")
    login()




def ask_todo_something_else():
    try:
        response = input("Would you like to do something else? Type Yes or No \n")
        if response.lower() == 'yes':
            login()
        elif response.lower() == 'no':
            print("Thanks for banking with us, Good bye!")
            exit()
        else:
            print('Invalid response')
            ask_todo_something_else()
    except Exception as e:
        print("something went wrong", e.__class__)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def deposit(acc_no):
    try:
        print("Enter Deposit Amount in digits")
        amount = int(input("How much do you want to deposit \n"))
        user = get_acc_details_from_database(acc_no)
        balance = user['balance']
        balance += amount
        print('You deposited %.2f' % amount)
        print("Your Account balance is %.2f" % balance)
        user['balance'] = balance
        update_account(acc_no, user)
        ask_todo_something_else()
    except Exception as w:
        print("something went wrong", w.__class__)


def withdraw_cash(acc_no):
    try:
        print('How much do you want to withdraw')
        print('Enter Amount in digit')
        amount = int(input("Amount to Withdraw \n"))
        user_balance = confirm_balance(acc_no)
        if user_balance < amount:
            print("Insufficient Fund")
        elif user_balance == amount:
            print('This amount is all you have in your account')
            print("Do you want to withdraw all?")
            response = input("Yes or No \n")
            if response.lower() == 'yes':
                user_balance -= amount
                print('take your cash')
                user = get_acc_details_from_database(acc_no)
                user['balance'] = user_balance
                update_account(acc_no, user)
                ask_todo_something_else()
            elif response.lower() == 'no':
                print('Enter new amount to withdraw')
                withdraw_cash(acc_no)
            else:
                print('Invalid response')
                exit()
        else:
            user_balance -= amount
            print('take your cash')
            user = get_acc_details_from_database(acc_no)
            user['balance'] = user_balance
            update_account(acc_no, user)
            ask_todo_something_else()
    except Exception as e:
        print("Something went wrong" , e.__class__)


def transfer_cash(acc_no):
    try:
        user = get_acc_details_from_database(acc_no)
        print("Enter Amount to transfer in digits")
        amount = int(input("How much do you want to transfer \n"))
        amount = validate_input_as_number(amount)
        print("Enter beneficiary account number in digits")
        beneficiary = input("Beneficiary account number \n")
        beneficiary = validate_to_tendigits(beneficiary)
        beneficiary = validate_input_as_number(beneficiary)
        user_balance = confirm_balance(acc_no)
        if user_balance < amount:
            print("Insufficient Fund")
        elif user_balance == amount:
            print('The amount is all you have in your account')
            print("Do you want to transfer all?")
            response = input("Yes or No \n")
            if response.lower() == 'yes':

                to_who = get_acc_details_from_database(beneficiary)
                to_who["balance"] += amount
                update_account(beneficiary, to_who)
                print('%.2f has been transferred to %' % (amount, beneficiary))
                user['balance'] -= amount
                update_account(acc_no, user)
                ask_todo_something_else()
            elif response.lower() == 'no':
                print('Enter new amount to transfer')
                transfer_cash(acc_no)
            else:
                print('Invalid response')
                exit()
        else:
            to_who = get_acc_details_from_database(beneficiary)
            to_who["balance"] += amount
            update_account(beneficiary, to_who)
            print('%.2f has been transferred to %' % (amount, beneficiary))
            user['balance'] -= amount
            update_account(acc_no, user)
            ask_todo_something_else()
    except Exception as e:
        print("something went wrong", e.__class__)


def get_balance(account_number):
    user = get_acc_details_from_database(account_number)
    balance = user['balance']
    print("Your Account balance is %.2f" % balance)


def confirm_balance(account_number):
    user = get_acc_details_from_database(account_number)
    balance = user['balance']
    return balance


def account_balance():
    account_number = int(input("Enter your Account Number \n"))
    user = get_acc_details_from_database(account_number)
    owner = user['account_number']
    balance = user['balance']
    if owner == account_number:
        print("Your account balance is: %.2f" % balance)
        ask_todo_something_else()
    else:
        print('Wrong Account Number supplied')
        account_balance()


