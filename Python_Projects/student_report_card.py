class Student:
    def __init__(self,stud_id,name,classname,marks):
        self.stud_id = stud_id
        self.name = name
        self.classname = classname
        self.marks = marks

    def total_marks(self):
        total=0
        for i in self.marks:
            total = total + i
        return total

    def average_marks(self):
        total=self.total_marks()
        average = total/len(self.marks)
        if average> 90 and average <= 100:
            return "O"
        elif average> 80 and average <= 90:
            return "A"
        elif average> 70 and average <= 80:
            return "B"
        elif average> 60 and average <= 70:
            return "C"
        elif average> 50 and average <= 60:
            return "D"
        elif average> 40 and average <= 50:
            return "E"
        elif average <= 40:
            return "Fail"

    def percentage_calculation(self,total):
        return (total/500)*100

    def report_card(self):
        grade=self.average_marks()
        total = self.total_marks()
        subjects=["AI","Web Mining","Computer Neworks","Operating Systems","Machine Learning"]
        print("#########----------REPORT CARD----------###########")
        print("Student ID:",self.stud_id)
        print("Name:",self.name)
        print("Classname:",self.classname)
        for subject,marks in zip(subjects,self.marks):
             print(f"{subject} : {marks}")
        print(f"Total Marks: {total}/500")
        print("Percentage :",self.percentage_calculation(total))
        print("Grade:",grade)
        print("#########----------END REPORT CARD----------###########")

    def report_card_file_addition(self, file=None):
        grade = self.average_marks()
        total = self.total_marks()
        subjects = ["AI", "Web Mining", "Computer Networks",
                    "Operating Systems", "Machine Learning"]

        lines = [
            "#########----------REPORT CARD----------###########",
            f"Student ID  : {self.stud_id}",
            f"Name        : {self.name}",
            f"Classname   : {self.classname}",
        ]
        for subject, marks in zip(subjects, self.marks):
            lines.append(f"  {subject} : {marks}")

        lines.append(f"Total Marks : {total}/500")
        lines.append(f"Percentage  : {self.percentage_calculation(total):.2f}%")
        lines.append(f"Grade       : {grade}")
        lines.append("#########----------END REPORT CARD----------###########")
        lines.append("")  # empty line between students

        for line in lines:
            if file:
                file.write(line + "\n")  # also writes to file


if __name__ == "__main__":
   number_of_students=int(input("Enter the number of students : "))
   student_object=[]
   for i in range(number_of_students):
       marks=[]
       stud_id=input("Enter Student ID : ")
       name=input("Enter Student Name : ")
       classname=input("Enter Student Class : ")

       for j in range(5):
           mark=int(input(f"Enter Mark {j+1} : "))
           marks.append(mark)
       s=Student(stud_id,name,classname,marks)
       student_object.append(s)

   for a in student_object:
       a.report_card()




