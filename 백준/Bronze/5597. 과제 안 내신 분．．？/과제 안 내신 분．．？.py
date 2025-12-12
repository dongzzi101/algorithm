import sys

students_number = []

for student in sys.stdin:
    students_number.append(int(student))

students_number.sort()

all_students_number = []

for _ in range(1, 31):
    all_students_number.append(_)

absent_student = []

for num in all_students_number:
    if num not in students_number:
        absent_student.append(num)

for _ in absent_student:
    print(_)