student_attendance = {'Rolf':96,'Bob':80,'Anne':100}


for student in student_attendance:
    print(f'{student} - {student_attendance[student]}')

    # or


for student, attendance in student_attendance.items():
    print(f'{student} - {attendance}')

if 'Bob' in student_attendance:
    print('present')