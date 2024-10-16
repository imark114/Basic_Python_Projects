# Grade Calculator: Calculate a student's grade based on their score using relational operators to determine the grade range.

score = float(input("Enter the student's score: "))

if score >= 90:
  grade = "A+"
elif score >= 85:
  grade = "A"
elif score >= 80:
  grade = "A-"
elif score >= 75:
  grade = "B+"
elif score >= 70:
  grade = "B"
elif score >= 65:
  grade = "B-"
elif score >= 60:
  grade = "C+"
elif score >= 55:
  grade = "C"
elif score >= 50:
  grade = "C-"
else:
  grade = "F"

print(f"The student's grade is: {grade}")