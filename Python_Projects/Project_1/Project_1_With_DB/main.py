from student import Student
from database import fetch_all_students,insert_students,update_grade_percentage

if __name__ == '__main__':
    number_of_students = int(input("Enter the number of students:"))
    for i in range(number_of_students):
        marks=[]
        student_id= input("Enter the student id:")
        student_name = input("Enter student name:")
        student_class = input("Enter student class:")

        for j in range(5):
            marks.append(float(input("Enter marks:")))

        insert_students(student_id,student_name,student_class,marks)

    rows = fetch_all_students()
    for row in rows:
        stud_id = row['stud_id']
        name = row['name']
        classname = row['classname']
        marks = [row['ai'], row['web_mining'], row['comp_networks'], row['os'], row['ml']]
        # ai, web_mining, comp_networks, os, ml

            # Use your Student class for calculation
        s = Student(stud_id, name, classname, marks)
        total = s.total_marks()
        percentage = s.percentage_calculation(total)
        grade = s.average_marks()

        # Store calculated values back to DB
        update_grade_percentage(stud_id, total, percentage, grade)

        # Print report card
        s.report_card()