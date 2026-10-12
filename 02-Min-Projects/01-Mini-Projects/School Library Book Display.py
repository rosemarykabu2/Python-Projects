books = ["Python Basics","Database Systems","JavaScript","Networking","Git & Github"]
borrowed_books = ["JavaScript","Networking"]

for book in books:
    if book in borrowed_books:
        continue
    print(f"Available Book: {book}")    
