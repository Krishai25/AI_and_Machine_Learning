class Employee_Application:
    def __init__(self,name,email,projects_handled,salary_expected):
        self.name=name
        self.email=email
        self.projects_handled=projects_handled
        self.salary_expected=salary_expected
        self.__salary_fixed=0
        self.__isAppointed = False
        self.employee_email=""
    def manager_view(self):
        return {
            "name":self.name,
            "email":self.email,
            "projects_handled":self.projects_handled,
            "salary_expected":self.salary_expected
        }
    def manager_process(self):
        if len(self.projects_handled) > 3 :
            self.__salary_fixed=self.salary_expected+500
            self.__isAppointed=True
            self.employee_email=self.name.replace(" ","")+"@company.com"

    def employee_profile_view(self):
        if self.__isAppointed :
            return {
                "Status": "Appointed",
                "name":self.name,
                "email":self.employee_email,
                "Salary":self.__salary_fixed
            }
        else :
            return{
                "Status": "Not Appointed",
                "name":self.name,
                "Reason": "Less No of Projects"
            }

class Manager_View:
    def __init__(self, emp):
        self.emp = emp

    def manager_view(self):
        return self.emp.manager_view()


class Candidate_View:
    def __init__(self, emp):
        self.emp = emp

    def candidate_view(self):
        self.emp.manager_process()
        return self.emp.employee_profile_view()

emp=Employee_Application("V S Krishai","krishai@gmail.com",["ML","LLM","FineTuning","Open Ai"],75000)
m=Manager_View(emp)
print("----- MANAGER VIEW -----")
print(m.manager_view())

c=Candidate_View(emp)
print("----- CANDIDATE VIEW -----")
print(c.candidate_view())