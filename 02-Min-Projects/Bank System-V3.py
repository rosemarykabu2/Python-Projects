accounts =[
     {
    "name":"Annabel",
    "balance":1500,
    "pin":36912
    },
    {
      "name":"Michael",
      "balance":2500,
      "pin":12345
    },
     {
          "name":"Rose",
          "balance":1000,
          "pin":67890
        }
]
def login():
  user_pin = int(input("Enter you PIN: "))
  for account in accounts:
     while user_pin != account['pin']:
            print("Incorrent pin!")
            user_pin = int(input("Enter your pin: "))
    
     if user_pin == account['pin']:
             return True
     else:
              return False
                     
                 
             
             
        

   
