# In this we will input the same for the report card generation of student by using the functionality of the class student
# from different file

from student_report_card import Student
if __name__ == "__main__":
   number_of_students=int(input("Enter the number of students : "))
   for i in range(number_of_students):
       marks=[]
       stud_id=input("Enter Student ID : ")
       name=input("Enter Student Name : ")
       classname=input("Enter Student Class : ")

       for j in range(5):
           mark=int(input(f"Enter Mark {j+1} : "))
           marks.append(mark)
       s=Student(stud_id,name,classname,marks)
       student_requirement=input("Enter Student Requirement : Console / Document File : ")
       if student_requirement == "Document File":
          with open (f"report_card{stud_id}.txt","a") as file:
             s.report_card_file_addition(file)
       else :
           s.report_card()

# It also Handles File Handling By Displaying the record either on console or document
