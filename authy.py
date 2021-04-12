import random

# -  Register
# _ username, email, password

#- userid  - gnerete user account
# - Login
# - (username or email), password

# bank operation

acountNumber = random._ceil(4545255 * 5)
database = {}

def init():
    print('Welcome to bankPHP')

    isSelectedOption = False

    while isSelectedOption == False:
        haveAccount = int(input("Do you have account with us> 1(yes) 2(no) \n"))
        if(haveAccount == 1):
            isSelectedOption == True
            login()
        elif(haveAccount == 2):
            isSelectedOption == True
            register()
            break
        else:
            print('You selected invalid option ')

def register():
    surName  =  input("What is your Surname \n ")
    firstName  =  input("What is your Firstname \n ")
    email  =  input("What is your email address \n ")
    username = input("Choose a username \n")
    password = input("Choose a password \n")
    accountNumber = generateAccountNumber()
    
    database[accountNumber] = {"surname":surName, "firstname":firstName, "username": username, "email":email, "password": password, "accountnumber": accountNumber}
    print('Your account has been created')

    details = database[accountNumber]
    print(details)
    login()
    

    
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def login():
    print('Login to your account')
    transaction()

def transaction():
    print('What would you like to do')

# ACTUAL BANKING SYSTEM

init()



