required_exam_code = "UPSA2026"

exam_code = input("Enter your exam code: ").upper()


while exam_code != required_exam_code:
    print("Wrong code, Try again")
    exam_code = input("Enter your exam code: ")
    
fee_confirmation = input("Hve you paid your examination fees(yes/no): ").lower()


if fee_confirmation == "yes":
        print("Exam access granted. \n Good luck!")
else:
         print("Access denied. Please pay your examination fees.")
    
    

