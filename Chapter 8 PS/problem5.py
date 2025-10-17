def removeWord(word, list):
    for w in list:
        w=w.strip()
        if w==word:
            list.remove(w)

    return list

list = ["apple", "banana", "watermelon", "grapes", "apple"]

list = removeWord("apple", list)

print(list)