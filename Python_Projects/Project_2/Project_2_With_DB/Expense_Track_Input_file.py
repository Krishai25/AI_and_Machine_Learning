from Expense_track import ExpenseTrack

class ExpenseTrackInput_file:
    def __init__(self):
        self.obj=ExpenseTrack()

    def addExpense(self):
        category_name=input("Enter Category Name: ")
        amount=float(input("Enter price: "))
        self.obj.add_expense(category_name,amount)

    def viewExpense(self):
        results = self.obj.view_all_expense()
        for i, row in enumerate(results, 1):
           print(f"{i}. {row[1]} - Rs. {row[2]} | Date: {row[3]}")
        print(f"Total Expense: Rs. {self.obj.get_total_of_the_expense()}")

    def getExpensebyCategoryName(self):
        category_name = input("Enter Category Name: ")
        results = self.obj.get_expense_by_category(category_name)
        if not results:
            print(f"No expenses found for: {category_name}")
            return
        for i, row in enumerate(results, 1):
            print(f"{i}. {row[1]} - Rs. {row[2]} | Date: {row[3]}")

    def highExpense(self):
        result = self.obj.get_highest_expense()
        print(f"Highest Expense → {result[1]} - Rs. {result[2]}")

    def exitExpense(self):
        self.obj.close()


