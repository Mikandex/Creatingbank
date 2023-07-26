import bankclass as bank
import  datetime

date = datetime.datetime

mydate = date.now()
data = []

while True:

    try:
        transaction_type = bank.transaction_type()

        if transaction_type == 'c':
            name = bank.name()
            age = bank.age()
            phone = bank.phone()
            create_account = bank.Person(name, age, phone, wallet=0)
            successful_created = create_account.registration_message()
            print(successful_created)
            data.append(name)
            data.append(age)
            data.append(phone)
            data.append(create_account.wallet)

        elif transaction_type == 'd':
            amount = bank.deposit()
            desposit = bank.Bank(mydate, full_name=data[0], age=data[1], phone_number=data[2], wallet=data[3])
            updated = data[3] + amount
            myupdate = data[3] = updated
            print(f'you deposited {myupdate} in your wallet and your total balance is {data[3]}')

        elif transaction_type == 'w':
            amount = bank.withdrawal_info()
            if amount > data[3]:
                print(f'you dont have enough balance {data[3]}')
            else:
                withdraw = bank.Bank(mydate, full_name=data[0], age=data[1], phone_number=data[2], wallet=data[3])
                updated_amount = withdraw.withdrawal(amount)
                data[3] = updated_amount
                print(f'you withdrew {amount} and your present balance is {data[3]}')
                data.append(amount)


        elif transaction_type == 'b':
            bal = bank.Bank(mydate, full_name=data[0], age=data[1], phone_number=data[2], wallet=data[3])
            print(bal.check_bal())

        elif transaction_type == 'p':
            name = data[0]
            age = data[1]
            phone = data[2]
            print(name, age, phone)
        elif transaction_type == 't':
            data_length = len(data)
            transaction_data = data[4: data_length]
            print(transaction_data)


        else:
            print('wrong input')

    except:
        print('you input the wrong data, you have not created account')



