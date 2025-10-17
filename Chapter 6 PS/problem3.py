p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

spam = input("Enter message: ")

if (p1 in spam) or (p2 in spam) or (p3 in spam) or (p4 in spam):
    print("This is spam")
else:
    print("No spam")