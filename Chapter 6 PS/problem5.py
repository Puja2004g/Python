list = ["apple", "orange", "banana", "grapes"]

name = input("Enter a fruit name: ")

for i in range(len(list)):
    if name in list[i]:
        print("Present")
        break
    else:
        print("Not present")