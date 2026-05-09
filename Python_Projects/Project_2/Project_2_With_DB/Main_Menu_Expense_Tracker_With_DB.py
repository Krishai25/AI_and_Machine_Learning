from Expense_Track_Input_file import ExpenseTrackInput_file

if __name__ == "__main__":
    object = ExpenseTrackInput_file()

    while True:
        print("1. Add expense")
        print("2. View expense")
        print("3. Highest expense")
        print("4. View by category")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Option 1. Add expense")
            object.addExpense()

        elif choice == "2":
            print("Option 2. View expense")
            object.viewExpense()

        elif choice == "3":
            print("Option 3. Highest expense")
            object.highExpense()

        elif choice == "4":
            print("Option 4. View by category")
            object.getExpensebyCategoryName()

        elif choice == "5":
            object.exitExpense()
            break
        else :
            print("Invalid Option")