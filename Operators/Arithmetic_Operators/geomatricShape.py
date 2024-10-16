# Geometric Shape Area Calculator: Compute the areas of various shapes like squares, rectangles, circles, and triangles.
import math

def area_of_square(side):
    return side*side

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    return math.pi * radius * radius

def area_of_triangle(base, height):
    return (base*height)/2

print("Choose the shape:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
  side = float(input("Enter the side of the square: "))
  area = area_of_square(side)
  print(f"Area of the square: {area}")
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_of_rectangle(length, width)
    print(f"Area of the rectangle: {area}")
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    print(f"Area of the circle: {area}")
elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_of_triangle(base, height)
    print(f"Area of the triangle: {area}")
else:
    print("Invalid choice.")