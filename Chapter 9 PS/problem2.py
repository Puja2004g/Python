import random

dict={
    "s":1,
    "w":-1,
    "g":0
}

n = int(input("How many times you want to play: "))

comMarks = 0
youMarks = 0

for i in range(n):
    computer = random.choice(list(dict.values()))
    # print(computer)
    num=input("Enter your choice (s,g,w): ")

    you = dict[num]

    if computer==1 and you==-1:
        # print("Computer win")
        comMarks+=1
    elif computer==-1 and you==0:
        # print("Computer wins")
        comMarks+=1
    elif computer==0 and you==1:
        # print("Computer wins")
        comMarks+=1
    elif  computer==-1 and you==1:
        # print("You wins")
        youMarks+=1
    elif computer==0 and you==-1:
        # print("You wins")
        youMarks+=1
    elif computer==1 and you==0:
        # print("You wins")
        youMarks+=1
    else:
        # print("Draw")
        comMarks+=1
        youMarks+=1

print(comMarks)
print(youMarks)

if comMarks>youMarks:
    result = "Computer wins"
elif youMarks>comMarks:
    result = "You win"
else:
    result = "Draw"


with open("Chapter 9 PS\\Hi-score.txt", "w") as f:
    f.write(f"Your marks: {youMarks}\n")
    f.write(f"Computer marks: {comMarks}\n")
    f.write(f"Result: {result}\n")