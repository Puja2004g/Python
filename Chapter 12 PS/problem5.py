num = int(input("Enter a number: "))

list = [num*i for i in range(1, 11)]

print(list)

with open("Chapter 12 PS\\table.txt", "a") as f:
    for value in list:
        f.write(str(value)+" ")
    f.write("\n")