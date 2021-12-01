from readFile import readFile

inputLines = readFile("input.txt")

inputLines = [int(i) for i in inputLines]

print(inputLines)

sums = []
for ii in range(0, len(inputLines)-2):
    sums.append(inputLines[ii]+inputLines[ii+1]+inputLines[ii+2])

print(sums)

numIncrease = 0
for ii in range(1, len(sums)):
    if sums[ii-1] < sums[ii]:
        numIncrease += 1

print(numIncrease)
