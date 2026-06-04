#A teacher is taking attendance of students.
#Strength of the class is 30.
#For each student, enter whether the student is Present or Absent.
#Count the total number of present and absent students.
#Display the attendance summary at the end.

student=30
attendance=0
present_students=0
absent_students=0

#---------------------------------------------------
#taking attendance of all students

while(attendance<student):

    attendance+=1

    status=input(f"Student {attendance} (P/A): ").strip().lower()

    #---------------------------------------------------
    #checking attendance status

    if(status=='p' or status=='present'):
        present_students+=1

    elif(status=='a' or status=='absent'):
        absent_students+=1

    else:
        print("Invalid input! Enter P for Present or A for Absent.")

        #repeating attendance for the same student
        attendance-=1

#---------------------------------------------------
#displaying attendance summary

print("\nAttendance Summary")
print("Present Students =",present_students)
print("Absent Students =",absent_students)
