# question 1
PI = 3.141592

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * PI * radius
area = PI * radius * radius

print(f"Circumference of the circle = {circumference}, Area of the circle = { area}", )
print()
print()

#question 2


n = 2

print(" a   n   a**n ")
print()

# Loop through values of a from 2 to 6
for a in range(2, 7):
    print(f" {a}   {n}   {a**n}")


