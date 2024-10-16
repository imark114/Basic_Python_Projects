# Number Comparison: Write a program that compares two numbers and determines if they are equal, greater than, or less than each other.

num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")