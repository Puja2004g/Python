with open("Chapter 9 PS\\log.txt", "r") as f:
    content = f.read()

with open("Chapter 9 PS\\copy.txt", "r") as c:
    copy = c.read()

if content == copy:
    print("Yes")

else:
    print("No")


