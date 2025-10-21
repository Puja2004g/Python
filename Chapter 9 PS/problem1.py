f = open("Chapter 9 PS\\poems.txt", "r")
text = f.read()

if "twinkle" in text:
    print("yes")
else:
    print("no")