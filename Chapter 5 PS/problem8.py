dict ={}

for i in range(4):
    key = input("Enter name: ")
    value = input("Enter fav. language: ")
    dict[key] = value

# duplicated values will not generate any error
# duplicate keys will generate error
print(dict.items())