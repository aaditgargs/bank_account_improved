print('This is Manhattan ATM')
bank_balance = 2000000
bank_balance_bela = 1000000
input('please enter your credit card and press enter if done')
accout_number = input('please enter your account no. ')
if accout_number == '20112011':
    print('Welcome Aadit')
    print('welcome to your account')

    print('your balance is $', int(bank_balance))
    atm = input('do you want to withdraw some money (y,n) ')
    if atm == 'y':
        withdrawel = input('how much money do want to withdraw ')
        bank_balance = int(bank_balance) - int(withdrawel)
        print('your balance is $', bank_balance)
    transfer = input('do you want to transfer some money to other accounts (y,n) ')
    if transfer == 'y':
        accout_transfer_name = input('who do you need to transfer ')
        if accout_transfer_name == 'Bela':
            accout_transfer = input('how much money do you need to transfer to Bela ')
            bank_balance = int(bank_balance_bela) + int(accout_transfer)
            bank_balance_bela = int(bank_balance) - int(accout_transfer)
            print('Bela has received ', accout_transfer)
            print(bank_balance)

elif accout_number == '166166':
    print('Welcome bela')
    print('welcome to your account')

    print('your balance is $', int(bank_balance))
    atm = input('do you want to withdraw some money (y,n) ')
    if atm == 'y':
        withdrawel_bela = input('how much money do want to withdraw ')
        bank_balance_bela = int(bank_balance_bela) - int(withdrawel_bela)
        print('your balance is $', bank_balance_bela)
        transfer = input('do you want to transfer some money to other accounts (y,n) ')
        if transfer == 'y':
            accout_transfer_name = input('who do you need to transfer ')
            if accout_transfer_name == 'Aadit':
                accout_transfer = input('how much money do you need to transfer to Aadit ')
                bank_balance = int(bank_balance) + int(accout_transfer)
                bank_balance_bela = int(bank_balance_bela) - int(accout_transfer)
                print('Aadit has received ', accout_transfer)
                print(bank_balance_bela)





else:
    print("let's continue with your day ")

