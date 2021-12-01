from readFile import readFile

inputLines = readFile("input.txt")

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

yes = []
for group in groups:
    for person in group:
        for ans in person:
            if ans not in yes:
                yes.append(ans)
    totalYes += len(yes)
    yes = []

print(totalYes)
