fruits = [
  "Apple\n",
  "Mango\n",
  "Orange"
]
with open("fruits.txt","w") as file:
  file.writelines(fruits)