# Number Validation: Validate if a number is within a specific range using logical operators to check multiple conditions.

num = int(input("Enter a number: "))

if num >= 0 and num <= 100:
  print("The number is within the range 0-100.")
else:
  print("The number is outside the range 0-100.")