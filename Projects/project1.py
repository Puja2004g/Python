# Snake water and Gun game
dict={
    "s":1,
    "w":-1,
    "g":0
}

# Snake beats Water (snake drinks water),
#  Water beats Gun (water drowns gun),
#  and Gun beats Snake (gun shoots snake)
computer = -1
num=input("Enter your choice (s,g,w): ")

you = dict[num]

if computer==1 and you==-1:
    print("Computer win")
elif computer==-1 and you==0:
    print("Computer wins")
elif computer==0 and you==1:
    print("Computer wins")
elif  computer==-1 and you==1:
    print("You wins")
elif computer==0 and you==-1:
    print("You wins")
elif computer==1 and you==0:
    print("You wins")
else:
    print("Draw")