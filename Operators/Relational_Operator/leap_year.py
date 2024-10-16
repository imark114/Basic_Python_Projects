# Leap Year Checker: Check if a given year is a leap year using the appropriate conditions involving modulus operators.

year = int(input("Enter a Year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")