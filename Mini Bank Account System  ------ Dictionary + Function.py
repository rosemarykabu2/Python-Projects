account = {
    "name":"Annabel",
    "balance":1500,
    "pin":36912
    }
def login():
    pin = int(input("Enter your pin: "))
    if pin == account['pin']:
        return True
    else:
        return False

result=login()

if result:
    print(f"Welcome,{account['name']}!")
else:
    print(f"Incorrect pin. Access denied.")

def check_balance(balance):
    return balance

current_balance= check_balance(account['balance'])

print(f"Your balance is {current_balance}")

def withdrawal(current_balance,withdrawal_amount):
    if withdrawal_amount <= current_balance:
        current_balance = current_balance - withdrawal_amount
        return current_balance
    else:
        return False
amount = withdrawal(current_balance,300)

if amount:
    print(f"Withdrawal successful. Current balance is {amount}")
    account['balance'] = amount
else:
    print("Withdrawal unsuccessful.")

def deposit(current_amount):
    deposit_money =int(input("Enter your deposit money: "))
    current_amount = current_amount + deposit_money
    print(f"Your deposit {deposit_money}, current balance {current_amount}")
    account['balance']=current_amount

deposit(account['balance'])  

    

   



