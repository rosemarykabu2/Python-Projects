account = {
    "name":"Annabel",
    "balance":150,
    "pin":36912
    }
def login():
    user_pin = int(input("Enter your pin: "))
    while user_pin != account['pin']:
        print("Incorrent pin!")
        user_pin = int(input("Enter your pin: "))

    if user_pin == account['pin']:
         return True
    else:
          return False
 
    
def check_balance(balance):
    return balance

def withdrawal(current_balance):
    withdrawal_amount = int(input("Enter your withdrawal amount: "))
    if withdrawal_amount <= current_balance and current_balance - withdrawal_amount >=10: 
        current_balance = current_balance - withdrawal_amount
        return current_balance
    else:
        return False    

def deposit(current_amount):
    deposit_money =int(input("Enter your deposit money: "))
    current_amount = current_amount + deposit_money
    print(f"Your deposit {deposit_money}, current balance {current_amount}")
    account['balance']=current_amount

result = login()

if result:
        running = True
        while running:
             print("1. Check balance")
             print("2. Withdraw")
             print("3. Deposit")
             print("Q. Quit")
                 
             choice = input("Choose an option: ")
                 
             if choice == "1":
                current_balance = check_balance(account['balance'])
                print(f"Your balance is {current_balance}")

             elif choice == "2":
               current_amount = withdrawal(account['balance'])
               if current_amount:
                  account['balance']= current_amount
                  print(f"Withdrawal successful, current balance is {current_amount}.")
               else:
                  print("Withdrawal failed, you don't have enough balance in your account.")

             elif choice =="3":
                deposit(account['balance']) 

             elif choice == "Q":
                 print("Q was detected")
                 running = False
                     
                 
             
             
        

   
