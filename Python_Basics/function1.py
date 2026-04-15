def add(a, b):
    return a + b


def remove_blankspace(word):
    new_word = "".join(word.strip().split())
    return new_word


def addargs(*args):
    total = 0
    for num in args:
        total = total + num
    return total

def create_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key}: {value}")



# 👇 This block runs ONLY when file is executed directly
if __name__ == "__main__":
    print(add(1, 2))
    print(remove_blankspace("      hello         world       "))

    result = addargs(1, 2, 3, 4, 5)
    print(result)
    print(create_profile(Name="V S Krishai", position="Manager", Company="Amazon"))