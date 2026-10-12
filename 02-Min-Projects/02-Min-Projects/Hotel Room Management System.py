hotel = [
    ["Available","Occupied","Available"],
    ["Occupied","Available","Occupied",]
    ]

for floor in range(len(hotel)):
    for room_num in range(len(hotel[floor])):
        print(f"Floor {floor+1}-Room {hotel[floor][room_num]}",end=" ")
    print()    

floor = int(input("Enter floor number: "))-1
room = int(input("Enter room number: "))-1
print(hotel[floor][room])

if hotel[floor][room] == "Available":
    hotel[floor][room] ="Occupied"
    print("Room booked successfully")
else:    
    print("Sorry, room is already occupied")

print(f"Floor {floor+1} - Room {room+1} {hotel[floor][room]}")    
