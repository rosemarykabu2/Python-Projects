minimum_age_requirement = 18
minimum_income_requirement = 2000

name = input("Enter your name: ")
age = int(input("Enter your age: "))
monthly_income = int(input("Enter your monthly income: "))

if age >= minimum_age_requirement:
    if monthly_income >= minimum_income_requirement:
        print("Loan Approved")
    else:
        print("Loan application rejected: Income requirement not met.")
else:
    print("Loan application rejected: Age requirement not met.")
    
