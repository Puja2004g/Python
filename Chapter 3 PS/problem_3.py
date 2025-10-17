text = input("Enter a text: ")
count=0

for i in range(len(text)-1):
    if text[i] == " " and text[i+1]==" ":
        count+=1


print(count)