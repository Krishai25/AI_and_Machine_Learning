mark1="80"
mark2="90"
mark3="85"

total=mark1+mark2+mark3
print(total)
# gives o/p as 809085
# 1. Convert strings to integers to get the sum
total = int(mark1) + int(mark2) + int(mark3)

# 2. Calculate the actual average
avg = total / 3

print("The sum is:", total)
print("The average is:", avg)

# Also learnt the in python there is no character data type but
# single letter or character is assumed as the string in python