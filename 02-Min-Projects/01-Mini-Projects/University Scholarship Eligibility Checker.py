required_score = 85
sports_status = "yes"

name = input("Enter your name: ")
score =int(input("Enter your score: "))
representation =input("Have your represented the university in national sports?(yes/no): ")

if score >= required_score or representation == sports_status:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")
