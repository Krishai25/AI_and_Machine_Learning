amount=500
tax=amount * 0.18
total=amount + tax
print(total)
if(total >= 800):
    discount=total*0.10
    total-=discount
    print(total)
else:
    print("No Discount")

# Logical Op
age=20
if(age >= 18 and age <= 25):
    is_student=True
else:
    is_student=False

if(is_student):
    print("Discount Applicable")
else:
    print("No Discount applicable")