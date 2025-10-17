text = input("Enter a text: ")

while "  " in text :
    text = text.replace("  ", " ")

print(text)