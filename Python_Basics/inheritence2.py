from Python_Basics.inheritence1 import Calculator
class calc3(Calculator):
    def mul(self,a,b):
        return a*b

c=calc3()
ans=c.mul(2,3)
print(ans)
ans=c.add(2,3)
print(ans)

"""The Calculatore mehod from the file inheritence1 is imported and functionality is implemented"""