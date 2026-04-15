age=18
if(age >= 18):
    print("ELigible to vote")
else:
    print("not eligible to vote")


marks = 39
if(marks >= 70 and marks <= 100):
    print("Grade A")
elif(marks >= 40 and marks < 70):
    print("Grade B")
else:
    print("Grade C")

order_amount=100
day="mon"
membership="silver"
if(order_amount >= 100 and day in["sat","sun"]) or membership == "gold":
    print("Discount of 20% applied")
else:
    print("Discount not applicable")

"""Newly learnt that in python the in keyword is used to check whether any of the 
word in input is present in the given set conditons
if day= sat and in[sat,sun] means if the day contains either sat or sun then the case is true"""