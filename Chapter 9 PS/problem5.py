words = ["Donkey", "slow-mover", "animal"]


with open("Chapter 9 PS\\essay_problem_4.txt", "r") as f:
    content = f.read()

for word in words:
    content  = content.replace(word, "#" * len(word))

with open("Chapter 9 PS\\essay_problem_4.txt", "w") as f:
    f.write(content)