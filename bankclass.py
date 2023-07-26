class Person:
    def __init__(self, full_name, age, phone_number, wallet):
        self.name = full_name
        self.age = age
        self.phone = phone_number
        self.wallet = wallet

    def registration_message(self):
        return f'congratulations {self.name} you have successful created account number with your phone number: {self.phone}'

class Bank(Person):
    def __init__(self, date, full_name , age, phone_number, wallet ):
        self.wallet = wallet
        self.date = date
        super().__init__(full_name, age, phone_number, wallet)
    def deposit(self, amout):
        self.wallet += amout
        return f'{self.wallet}'
    def withdrawal(self, amount):
        self.wallet -= amount
        return self.wallet
    def check_bal(self):
        return 'your balance is {}'.format(self.wallet)



def age():
    age = int(input('What is your age number only e.g 18? \n'))
    if age > 99:
        print('Your not allowed to create acount based on our company policy')
    elif age < 18:
        print(' you are not allowed to create account base on regulation')

    return age

def phone():
    my_phone = input('What is your phone number dont include the first 0, it must be 10 digits? \n')
    if len(my_phone) > 10:
        nphone = int(my_phone)
        print(f'it must be 10 {nphone} ')
    if len(my_phone) < 10:
        nphone = int(my_phone)
        print(f'It must be 10 {nphone}')
    else:
        nphone = int(my_phone)
        return nphone



def name():
    my_name = input('What is your name?\n')
    return my_name

def deposit():
    my_deposit = int(input('what is the amount you want to desposit must be number? \n'))
    return my_deposit
def transaction_type():
    t = input(
            "What's transaction to you want to perform? \n c: create account, d: Deposit, w: withdraw, b: Balance, t: transactional Data "
            "p: Profile\n")
    return t
def withdrawal_info():
    dep = int(input('what is the amount you want to withdraw? \n'))
    return dep