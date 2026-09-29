import math 
radius = int(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi  * radius ** 2

print("=====================")
print("CIRCLE REPORT")
print("=====================")

print(f"Radius: {radius}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")

print("=======================================")
