# Voting Eligibility Checker: Determine if a person is eligible to vote based on their age and citizenship status using logical operators to combine conditions.

age = int(input("Enter your age: "))
citizenship = input("Are you a citizen of this country? (yes/no): ")

if age >= 18 and citizenship.lower() == 'yes':
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote")