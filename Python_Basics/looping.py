n=5
names=["Alice","Bob","Charlie","David"]
pin="7777"
enteredpin=""
for name in names:
    print(name.upper())

while enteredpin!=pin:
    enteredpin=input("Enter your pin: ")

print("Access Granted")

for i in range(n):
    for j in range(i) :
        print("*",end="")
    print()

for i in range(n):
    for j in range(n-i) :
        print("*",end="")
    print()

people=[0,0,0,1,0,0,0]
len=len(people)
print(len)
count=0
for thief in people:
    if thief==1:
        break
    count+=1
print(f"normal people before thief {count}")

count1=0
for thief in people:
    if thief==1:
        continue
    count1+=1

print(f"normal people after thief found{count1}")

