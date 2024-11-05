students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [88, 92, 80]},
    {"name": "Charlie", "grades": [95, 85, 82]},
]

def calculate_average(grades):
    return sum(grades) / len(grades)

with open("students_average_grades.txt", "w") as file:
    for student in students:

        avg_grade = calculate_average(student["grades"])
        file.write(f"{student['name']} - Average Grade: {avg_grade:.2f}\n")

print("Average grades have been written to 'students_average_grades.txt'.")
