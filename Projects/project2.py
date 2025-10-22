import random

comp = random.randint(1,100)
a=-1
guess = 0

while a != comp:
    guess+=1
    user = int(input())

    if user > comp:
        print("Lower number please")
    elif user < comp:
        print("Higher number please")
    else:
        print(f"Correct : {guess}")
    