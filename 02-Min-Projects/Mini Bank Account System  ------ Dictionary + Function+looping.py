account = {
    "name":"Annabel",
    "balance":1500,
    "pin":36912
    }
def login():
    user_pin = int(input("Enter your pin: "))
    while user_pin != account['pin']:
        print(f"Incorrect pin.")
        user_pin=int(input("Enter your pin: "))
    

    if user_pin == account['pin']:
        print(f"Welcome, {account['name']}!") 
        return True
    else:
        return False
result = login()

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
if result: 
    amount = withdrawal(current_balance,300)
    if amount:
         print(f"Withdrawal successful. Current balance is {amount}")
         account['balance'] = amount
    else:
        print("Withdrawal unsuccessful.")        

def deposit(current_amount):
    if result:
        deposit_money =int(input("Enter your deposit money: "))
        current_amount = current_amount + deposit_money
        print(f"Your deposit {deposit_money}, current balance {current_amount}")
        account['balance']=current_amount
deposit(account['balance'])  

    

   



