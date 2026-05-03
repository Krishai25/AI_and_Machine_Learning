number=int(input("Enter a number: "))
try:
    division=10/number
    print(division)
except ZeroDivisionError:
    print("Division by zero - Number should be greater than 0")
    print(ZeroDivisionError)
try:
 with open("file1.txt","r") as f:
    for line in f:
        print(line)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)