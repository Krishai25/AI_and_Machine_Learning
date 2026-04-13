class Student_Record:
    def __init__ (self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def display(self):
        print(f"Name : {self.name}  Age: {self.age}  Score: {self.score}")

"""for i in range(2):
    name= input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    score = int(input("Enter Student Score: "))
    s1=Student_Record(name,age,score)
    s1.display() """

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def square(self,a):
        return a**2
    def square_root(self,a):
        return a**(1/2)

c1=Calculator()
print(c1.add(1,2))
print(c1.sub(3,4))
print(c1.mul(3,4))
print(c1.div(3,4))
print(c1.square(3))
print(c1.square_root(3))

