from readFile import readFile

inputLines = readFile("input.txt")

questions = "abcdefghijklmnopqrstuvwxyz"

groups = []
group = []

for line in inputLines:
    if line != "":
        group.append(line)
    else:
        groups.append(group)
        group = []

#print(groups)

totalYes = 0

for group in groups:
    yes = set(questions).intersection(*group)
    totalYes += len(yes)

print(totalYes)
