from readFile import readFile

inputLines = readFile("input.txt")

maxID = 0
rowMax = 127
colMax = 7

for line in inputLines:
    rowMin = 0
    rowMax = 127

    colMin = 0
    colMax = 7

    rowInput = line[:6]
    colInput = line[7:]

    for pos in rowInput:
        if pos == 'F':
            rowMax = int((rowMin+rowMax)/2)
        elif pos == 'B':
            rowMin = int((rowMin+rowMax)/2)
    row = int((rowMin+rowMax)/2)
    #print(row)

    for pos in colInput:
        if pos == 'L':
            colMax = int((colMin+colMax)/2)
        elif pos == 'R':
            colMin = int((colMin+colMax)/2)
    col = int((colMin+colMax)/2)
    #print(col)

    seatID = row*8+col
    #print(seatID)
    if seatID > maxID:
        maxID = seatID

print(maxID)
