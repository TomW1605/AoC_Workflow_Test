from readFile import readFile

inputLines = readFile("Day3.txt")

grid = []

for line in inputLines:
    grid.append(list(line))

xCord = 0
xIncs = [1, 3, 5, 7]
treesTotal = 1

for xInc in xIncs:
    trees = 0
    for line in grid:
        if line[xCord] == '#':
            trees += 1
        xCord += xInc
        if xCord >= len(line):
            overflow = xCord-len(line)
            xCord = overflow
    print(str(xInc)+": "+str(trees))
    treesTotal *= trees
    xCord = 0

trees = 0
for lineNum in range(0,len(grid),2):
    line = grid[lineNum]
    if line[xCord] == '#':
        trees += 1
    xCord += 1
    if xCord >= len(line):
        overflow = xCord-len(line)
        xCord = overflow
print("1,2: "+str(trees))
treesTotal *= trees

print(treesTotal)
