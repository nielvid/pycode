allowedUsers = ['Godson', "Kate", "Deray"]
allowedPassword = ['123456', 'deray@08', '2016']
name = input("what is your name ")
if(name in allowedUsers):   
    password = input("Password ")
    userId = allowedUsers.index(name)
    if(password == allowedPassword[userId]):
        print( "Welcome %s " % name)
        print('What do you want to do ')
        print('Available options are:')
        print('1. Check Balance')
        print('2. Withdraw Cash')
        print('3. Deposit Cash')
        print('4. Print Statement')
        
        transaction = int(input('Select an option: '))
        if(transaction == 1):
            print('Your balance is: N5, 000') 
        elif(transaction ==2 ):
            pass 
        elif(transaction == 3):
            pass 
        elif(transaction == 4):
            pass 
        else:
            print('Invalid option, try again')
    else:
        print("Incorrect Password")
else:
    print('Name not found')
