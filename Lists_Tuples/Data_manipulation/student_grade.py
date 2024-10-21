# Student Grade Calculator: Create a program that takes student names and their scores in different subjects. Store the data in a list of tuples. Calculate the average score for each student and determine the highest and lowest scores.

def calculate_student_grades(student_data):
    result = []

    for st_name, scores in student_data:
        avarage_score = sum(scores) / len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        result.append((st_name, avarage_score, highest_score, lowest_score))
    return result

student_data = [
    ('Rakib', [85, 90, 78]),
    ('Kibriya', [90, 84, 75]),
    ('Mrunal', [92, 87, 79])
]

grades = calculate_student_grades(student_data)

for student in grades:
    print(f"{student[0]}'s avarage score: {format(student[1], '.2f')}, heighest score: {student[2]}, lowerst score: {student[3]}")