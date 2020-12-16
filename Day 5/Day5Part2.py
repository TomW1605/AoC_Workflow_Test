import math

from readFile import readFile

inputLines = readFile("input.txt")

seatIDs = []

for line in inputLines:
    rowMin = 0
    rowMax = 127

    colMin = 0
    colMax = 7

    rowInput = line[:6]
    colInput = line[7:]

    for pos in rowInput:
        if pos == 'F':
            rowMax = math.floor((rowMin+rowMax)/2)
        elif pos == 'B':
            rowMin = math.ceil((rowMin+rowMax)/2)
    if pos == 'F':
        row = rowMax
    elif pos == 'B':
        row = rowMin
    #print(row)

    for pos in colInput:
        if pos == 'L':
            colMax = math.floor((colMin+colMax)/2)
        elif pos == 'R':
            colMin = math.ceil((colMin+colMax)/2)
    if pos == 'L':
        col = colMax
    elif pos == 'R':
        col = colMin
    #col = int((colMin+colMax)/2)
    #print(col)

    seatID = row*8+col
    seatIDs.append(seatID)

seatIDs.sort()
print(seatIDs)

for ii in range(1, len(seatIDs)-1):
    if seatIDs[ii] == seatIDs[ii-1]+1 and seatIDs[ii] == seatIDs[ii+1]-1:
        print(seatIDs[ii])
