# Bitwise Calculator: Create a program that performs bitwise operations like AND, OR, XOR, NOT, left shift, and right shift on binary numbers.

def bitwise_and(x,y):
    return x & y

def bitwise_or(x,y):
    return x | y

def bitwise_xor(x, y):
    return x ^ y

def bitwise_not(x):
    return ~x

def left_shift(x,n):
    return x << n

def right_shift(x,n):
    return x >> n

print("Select operation:")
print("1. AND")
print("2. OR")
print("3. XOR")
print("4. NOT")
print("5. Left Shift")
print("6. Right Shift")

choice = int(input("Enter choice (1-6): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
  result = bitwise_and(num1, num2)
  print(f"Bitwise AND: {bin(result)}")
elif choice == 2:
  result = bitwise_or(num1, num2)
  print(f"Bitwise OR: {bin(result)}")
elif choice == 3:
  result = bitwise_xor(num1, num2)
  print(f"Bitwise XOR: {bin(result)}")
elif choice == 4:
  result = bitwise_not(num1)
  print(f"Bitwise NOT: {bin(result)}")
elif choice == 5:
  shift_amount = int(input("Enter shift amount: "))
  result = left_shift(num1, shift_amount)
  print(f"Left Shift: {bin(result)}")
elif choice == 6:
  shift_amount = int(input("Enter shift amount: "))
  result = right_shift(num1, shift_amount)
  print(f"Right Shift: {bin(result)}")
else:
  print("Invalid input")