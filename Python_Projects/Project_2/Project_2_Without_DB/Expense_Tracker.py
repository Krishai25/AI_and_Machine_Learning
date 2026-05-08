class Expense:

    def __init__(self):
        self.expense = []

    def add_expense(self, category_name, price):
        exp = {"category": category_name, "price": price}
        self.expense.append(exp)

    def sum_of_expense(self):
        total = 0
        for amount in self.expense:
            total += amount["price"]
        return total

    def highest_expense(self):
        if not self.expense:          # ← guard clause
            return "No expenses added yet"
        maxexpense = 0
        name = ""
        for expense in self.expense:
            if expense["price"] > maxexpense:
                maxexpense = expense["price"]
                name = expense["category"]
        return f"Category : [{name}] has the highest expense of Rupees: {maxexpense}"

    def view_by_category(self,category):
        sub_total=0
        l=[]
        for expense in self.expense:
            if expense["category"] == category:
                sub_total += expense["price"]
                view={"name":category, "price":expense["price"]}
                l.append(view)

        if not l:  # ← guard
            print(f"No expenses found for: {category}")
            return 0

        for i, e in enumerate(l, 1):
            print(f"{i}. {e['name']} - Rs. {e['price']}")  # ← fixed key

        print(f"Rs. {sub_total}")
        return None

    def disp(self):
        for i, e in enumerate(self.expense, 1):   # ← formatted display
            print(f"{i}. {e['category']} - Rs. {e['price']}")

        print(f"Total Expenses = Rs. {self.sum_of_expense()}")