students_scores= {
    "Mamad": 92,
    "Sepehr": 75,
    "Sina": 85,
    "Iman": 69,
}
students_grades = {}
for key in students_scores:
    if grade > 91:
        grade = "Outstanding"
    elif 81 < grade <= 90:
        grade = "Exeeds Expectations"
    elif 71 < grade <= 80:
        grade = "Acceptable"
    else:
        grade = "fail"
    students_grades[key] = grade

print(students_grades)
