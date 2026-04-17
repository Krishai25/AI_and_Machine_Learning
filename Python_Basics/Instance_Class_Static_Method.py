class MyClass:
    def instace_method(self):
        print("Called Instace Method")

    @classmethod
    def class_method(cls):
        print("Called Class Method")
    @staticmethod
    def static_method():
        print("Called Static Method")

obj=MyClass()
obj.instace_method()
MyClass.class_method()
MyClass.static_method()

class Company:
    company_name="OpenAI"
    @classmethod
    def change_name_company(cls,newname):
        cls.company_name=newname

    @staticmethod
    def try_changing_company_name(newname):
        company_name=newname
        print(company_name)
    # this will not work and change the company name

# Changing the class variable is possible by using the class method but it is not possible
# to change if the method is given as static
print(f"Before changing by ClassMethod- {Company.company_name}")
Company.change_name_company("Google")
print(f"After changing by ClassMethod- {Company.company_name}")

print(f"Before changing by StaticMethod- {Company.company_name}")
Company.try_changing_company_name("Apple") #We Get output as the company name Apple because i have
#printed the local variable changes by it does not change the class variable
print(f"After changing by StaticMethod- {Company.company_name} ")


