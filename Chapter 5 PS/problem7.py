dict ={}

for i in range(4):
    key = input("Enter name: ")
    value = input("Enter fav. language: ")
    dict[key] = value

# only unique values will be added
print(dict.items())