#first method from the console
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("The sum is:", a+b)

#Second Method
import sys
full_name=sys.argv[1]
"""
Variation 1 is of giving full_name=" ".join(sys.argv[1:] 
--> In the terminal it will take completely like V S Krishai and o/p as v.s.krishai

Variation 2 is of like using the python "path""name" in the terminal 
--> this will alsp o/p the same for the given input  python input.py "V S Krishai"
o/p -> vskrishai 
"""
email=full_name.lower().replace(" ",".")+"@amazon.com"
print("Your Profile")
print("Your Name:",full_name)
print("Your Email:",email)

