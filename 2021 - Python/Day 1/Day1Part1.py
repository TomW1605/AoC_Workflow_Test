from readFile import readFile

inputLines = readFile("input.txt")

inputLines = [int(i) for i in inputLines]

print(inputLines)

numIncrease = 0
for ii in range(1, len(inputLines)):
    if inputLines[ii-1] < inputLines[ii]:
        numIncrease += 1

print(numIncrease)
