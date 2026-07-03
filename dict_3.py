exams = [
    {"name": "Иван", "subject": "Math", "grade": 4},
    {"name": "Мария", "subject": "Math", "grade": 5},
    {"name": "Иван", "subject": "Physics", "grade": 3},
    {"name": "Иван", "subject": "Math", "grade": 5},
]
students_grades = {}
for exam in exams:
    name = exam["name"]
    subject = exam["subject"]
    grade = exam["grade"]
    if name not in students_grades:
        students_grades[name] = (subject, grade)
    else:
        old_grade = students_grades[name][1]
        if grade > old_grade:
            students_grades[name] = (subject, grade)
print(students_grades)
