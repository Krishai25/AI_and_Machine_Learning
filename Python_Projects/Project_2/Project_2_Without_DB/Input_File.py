from Expense_Tracker import Expense

class Input:

    def __init__(self):
        self.a=Expense()
    def add_exp(self):
        category=input("Enter category of expense : ")
        price=float(input("Enter price of expense : "))
        self.a.add_expense(category,price)

    def view_expense(self):
        self.a.disp()

    def high(self):
        print(self.a.highest_expense())

    def view_category(self):
        name=input("Enter name of category : ")
        self.a.view_by_category(name)


