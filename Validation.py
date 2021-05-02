
def validate_input_as_number(data):
    try:
        data = int(data)
        if type(data) == int:
            return data
        else:
            raise TypeError
    except TypeError:
        print("Input must be a Number")

def validate_to_tendigits(data):
    try:
        account_number = data
        if len(account_number) < 10:
            raise Exception
        elif len(account_number) > 10:
            raise Exception
        else:
            return account_number
    except Exception as e:
        print("Account Number must be Ten digits")
        return False

