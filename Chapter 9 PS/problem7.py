count=0

with open("Chapter 9 PS\\log.txt", "r") as f:
    for line in f:
        if "python" in line.lower():
            count+=1

print(count)