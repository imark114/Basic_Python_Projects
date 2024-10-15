# Interest Calculator: Calculate simple and compound interest based on user input.

def simple_interest(principal, rate, time):
  return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * (1 + rate/100) ** time - principal


print("Choose the type of interest:")
print("1. Simple Interest")
print("2. Compound Interest")

choice = int(input("Enter your choice (1/2): "))

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

if choice == 1:
  interest = simple_interest(principal, rate, time)
  print(f"Simple Interest: {interest}")
elif choice == 2:
  interest = compound_interest(principal, rate, time)
  print(f"Compound Interest: {interest}")
else:
  print("Invalid choice.")