grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed = []
for grade in grades:
    if (grade >= 60):
        grade = grade*1.05
        passed.append(grade)
print("Grades after filtering and applying bonus: ",passed)