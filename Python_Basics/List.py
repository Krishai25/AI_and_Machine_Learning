"""List are Mutable, Various Datatypes can be stored in a list"""

playlist=["Shape of You","Skyfall","Despacito","Despacito","Save your Tears"]
favourite_food=["Dosa","Briyani","Shawarma","Ice Cream"]

print(playlist)
print(favourite_food)

print(playlist.count("Despacito"))
print(playlist.pop(1))
playlist.sort()
print(playlist)
playlist.reverse()
print(playlist)
playlist.insert(2,"Madona")
playlist.append("Tum hi ho")
print(playlist)
new_playlist=playlist.copy()
print(new_playlist)
playlist.extend(favourite_food)
print(playlist)
playlist.clear()
print(playlist)

for item in favourite_food:
    print(item)

for i,items in enumerate(favourite_food):
    print(f"Position Number {i} : {items} ")

cart_item=[]
print("Enter the items and enter Done to end")
while True:
    word=input("Enter the item")
    if word == "Done":
        break
    else:
        cart_item.append(word)

print(cart_item)


"""
O/P:
['Shape of You', 'Skyfall', 'Despacito', 'Despacito', 'Save your Tears']
['Dosa', 'Briyani', 'Shawarma', 'Ice Cream']
2
Skyfall
['Despacito', 'Despacito', 'Save your Tears', 'Shape of You']
['Shape of You', 'Save your Tears', 'Despacito', 'Despacito']
['Shape of You', 'Save your Tears', 'Madona', 'Despacito', 'Despacito', 'Tum hi ho']
['Shape of You', 'Save your Tears', 'Madona', 'Despacito', 'Despacito', 'Tum hi ho']
['Shape of You', 'Save your Tears', 'Madona', 'Despacito', 'Despacito', 'Tum hi ho', 'Dosa', 'Briyani', 'Shawarma', 'Ice Cream']
[]
Dosa
Briyani
Shawarma
Ice Cream
Position Number 0 : Dosa 
Position Number 1 : Briyani 
Position Number 2 : Shawarma 
Position Number 3 : Ice Cream 
Enter the items and enter Done to end
Enter the item Noodle
Enter the itemsoap
Enter the itembrush
Enter the itembuiscuit
Enter the itemperfume
Enter the itemDone
[' Noodle', 'soap', 'brush', 'buiscuit', 'perfume']

"""


sample=[]
n = 6
for i in range(n):
    number=int(input())
    sample.append(number)

print(sample)

sample=[]
n=6
while n != 0:
    number=int(input())
    sample.append(number)
    n=n-1

print(sample)
even=0
odd=0
for i,number in enumerate(sample):
    if i%2 == 0 :
        even+=number
    else :
        odd+=number
print(abs(even-odd))
