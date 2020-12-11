from readFile import readFile

inputLines = readFile("Day3.txt")

grid = []

for line in inputLines:
    grid.append(list(line))

xCord = 0
trees = 0

for line in grid:
    if line[xCord] == '#':
        trees += 1
    xCord += 3
    if xCord >= len(line):
        overflow = xCord-len(line)
        xCord = overflow

print(trees)
