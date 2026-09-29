def calculate():
   first_num=int(input("Enter your first number: "))
   second_num=int(input("Enter your second number: "))
   operator = input("Enter your operator (+,-,*,/): ")
   
   
   if operator == "+":
       result = first_num + second_num
       print(f"{first_num} + {second_num} = {result}")
       
   elif operator == "-":
      result = first_num - second_num
      print(f"{first_num}-{second_num} = {result}")
      
   elif operator == "*":
       result = first_num * second_num
       print(f"{first_num}*{second_num} = {result}")
       
   elif operator =="/":
      result = first_num / second_num
      print(f"{first_num} / {second_num} = {result}")
   else:
      print("Invalid")
   
calculate()   
