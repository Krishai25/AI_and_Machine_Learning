name=input("Enter your Name :")
feedback = input("Enter your feedback :")


with open("feedback_log.txt","a") as file:
    file.write(f"\n{name} : {feedback}")
print("Thanks for your Valuable FeedBack")