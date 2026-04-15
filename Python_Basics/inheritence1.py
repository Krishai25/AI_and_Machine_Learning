"""These Represent the Multi level inheritence"""
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

class calc1(Calculator):
    def floor_number(self,number):
        return int(number)

class square_of_num(calc1):
    def square_of_num(self,number):
        return number*number

c1=calc1()
ans1=(c1.add(1.5,2.55))
print(ans1)
result1=c1.floor_number(ans1)
print(result1)

c2=square_of_num()
ans2=(c2.add(1.5,2.55))
print(ans2)
result2=c2.square_of_num(ans2)
print(c2.floor_number(result2))

"""These represent Multiple inheritence"""
class Dad:
    def property(self):
        print ("Dad's Property")
class Mom:
    def gold(self):
        print("Moms Gold")
class Son(Dad,Mom):
    def car(self):
        print("Son's Car")

s=Son()
s.car()
s.gold()
s.property()



"""This case particularly represen the Multiple Inheritence problem resolved in java
The Clas which is claeed first to inherit will be executing th particular call method if both 
class has same method name"""


class Dad:
    def gold(self):
        print("Dad's Property")


class Mom:
    def gold(self):
        print("Moms Gold")


class Son(Dad, Mom):
    def car(self):
        print("Son's Car")


s = Son()
s.car()
s.gold()

