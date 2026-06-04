#attendance counter

student=int(input("Enter the number of students in the class: "))

#validate number of students
if(student<0):
    exit("Invalid input. Number of students cannot be negative.")

#---------------------------------------------------
attendance=1

while(attendance<=student):
    print("Attendance count:",attendance)
    attendance+=1
