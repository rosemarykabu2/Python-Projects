#Find a Student in a Classroom
classroom =[
    ["Rose","Daniel","Mary"],
    ["John","Sarah","David"],
    ["Michael","Emma","Peter"]
    ]

name=input("Enter student's name: ")

found = False

for row in classroom:
    for student in row:
        if name == student:
            found =True
            print("Student found!")
            break
if found == False:
        print("Student not found")
