with open("chapter 9 PS\\essay_problem_4.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "#####")
content = content.replace("donkey", "#####")

with open("chapter 9 PS\\essay_problem_4.txt", "w") as f:
    f.write(content)

