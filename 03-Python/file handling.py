with open("python_notes.txt","w") as file:
  file.write("Welcome to Ghana!")

with open("python_notes.txt","a") as file:
  file.write("\n I am learning the Ghanaian culture.") 

with open("python_notes.txt","a") as file:
  file.write("\nGhana has many beautiful traditions.")  

with open("python_notes.txt","r") as file: 
  content = file.readlines()

for line in content:
  print(line, end="")  