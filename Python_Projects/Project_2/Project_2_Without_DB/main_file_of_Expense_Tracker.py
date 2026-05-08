from Input_File import Input

if __name__ == "__main__":
    i = Input()
    while True:
        print("1. Add expense")
        print("2. View expense")
        print("3. Highest expense")
        print("4. View by category")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Option 1. Add expense")
            i.add_exp()

        elif choice == "2":
            print("Option 2. View expense")
            i.view_expense()

        elif choice == "3":
            print("Option 3. Highest expense")
            i.high()

        elif choice == "4":
            print("Option 4. View by category")
            i.view_category()

        elif choice == "5":
            print("Exited successfully")
            break
