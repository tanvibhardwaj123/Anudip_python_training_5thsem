# a teacher is taking attendance of students. strength of class is 30 , every time he needs to insert whether students is present or absent . count the total number of students present in the class and display it at the end of the class as wlll as absent  students.        
student = 30
attendance = 0
present_students = 0
absent_students = 0

while attendance < student:
    attendance += 1

    status = input(f"Student {attendance} (P/A): ").strip().lower()

    if status == 'p' or status == 'present':
        present_students += 1

    elif status == 'a' or status == 'absent':
        absent_students += 1

    else:
        print("Invalid input! Enter P for Present or A for Absent.")
        attendance -= 1

print("\nAttendance Summary")
print("Present Students =", present_students)
print("Absent Students =", absent_students)
