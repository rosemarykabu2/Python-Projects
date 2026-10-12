movies = ["Avatar","Mufasa","Superman","Elio","Moana"]

name = input("Enter the movie you want to watch: ")

found = False

for movie in movies:
    if name == movie:
        print("Movie available!")
        break
if found == False:
    print("Sorry, this movie is not available today.")
