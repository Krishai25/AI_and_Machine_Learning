manager_name="V S Krishai"
print(manager_name.upper())
print(manager_name.lower())
print(manager_name.title())
print(manager_name.capitalize())

location="Coimbatore"
new_location=location.replace("Coimbatore","Erode")
print(new_location)

word="*****Airport*****"
print(word)
print(word.strip("*"))
print(word.lstrip("*"))
print(word.rstrip("*"))

message_uber="Your Uber Id is : UB12345 and Please Keep it safe"
uberid=message_uber.split(":")[1].lstrip().split("and")[0].rstrip()
print(uberid)

feedback="The drive was good and peacefull"
position_of_drive=feedback.find("drive")
print("Position is : " ,position_of_drive)

initials=" ".join(word[0].upper() for word in manager_name.split())
print(initials)

Sentence="HI How are you"
length=len(Sentence)
lengthofwords=len(Sentence.split(" "))
print(lengthofwords)
print(length)