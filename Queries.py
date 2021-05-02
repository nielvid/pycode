
def create_account(acc_id, data):
    try:
        acc_id = str(acc_id)
        f = open('data/' + acc_id + '.txt', 'w')
        f.write(str(data))
    finally:
        f = open('data/' + acc_id + '.txt')
        f.close()


def update_account(acc_id, data):
    try:
        acc_id = str(acc_id)
        f = open('data/' + acc_id + '.txt', 'w')
        update = f.write(str(data))
        return update
    finally:
        f = open('data/' + acc_id + '.txt')
        f.close()


def read_from_database(acc):
    try:
        acc = str(acc)
        f = open('data/' + acc + '.txt', 'r')
        res = f.read()
        to_dict = eval(res)
        return to_dict
    finally:
        f = open('data/' + acc + '.txt')
        f.close()


def get_acc_details_from_database(acc):
    try:
        acc = str(acc)
        f = open('data/' + acc + '.txt', 'r')
        res = f.read()
        to_dict = eval(res)
        return to_dict
    finally:
        f = open('data/' + acc + '.txt')
        f.close()


def loop_tru_database(acc):
    try:
        if acc in database:
            user = database[acc]
            return user
        else:
            raise LookupError
    except LookupError:
        print("Account Number does not exist in our bank")



database = {8692483462: {"surname": "Jide", "firstname": "Lucky", "username": "jide1", "email": "jide@gmail.com",
                         "password": '123456', "account_number": 8692483462, "balance": 500.00}}