students = ["Rose","Daniel","Mary","John","Sarah"]
name = input("Enter your name: ")

found = False
for student in students:
    if student == name:
        found = True
        print("Student found! \n Attendance marked successfully.")
        break
if found == False:
    print("Sorry, you are not registered for attendance.")
