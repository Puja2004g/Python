with open("Chapter 9 PS\\log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes")
else:
    print("No")