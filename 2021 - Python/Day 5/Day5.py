from readFile import readFile
from collections import Counter

def part1(input_lines):
    print(input_lines)

    points = []
    for line in input_lines:
        start, end = line.split(" -> ")
        startX, startY = [int(item) for item in start.split(",")]
        endX, endY = [int(item) for item in end.split(",")]

        if startX == endX:
            for y in range(endY if startY > endY else startY, (startY if startY > endY else endY)+1):
                points.append(str([startX, y]))
        elif startY == endY:
            for x in range(endX if startX > endX else startX, (startX if startX > endX else endX)+1):
                points.append(str([x, startY]))
        #print(line)
        #print(points)

    pointsCount = Counter(points)
    overlaps = 0
    for key in pointsCount:
        if pointsCount[key] > 1:
            overlaps += 1
    print(overlaps)

def part2(input_lines):
    print(input_lines)

    points = []
    for line in input_lines:
        start, end = line.split(" -> ")
        startX, startY = [int(item) for item in start.split(",")]
        endX, endY = [int(item) for item in end.split(",")]

        if startX == endX:
            for y in range(endY if startY > endY else startY, (startY if startY > endY else endY)+1):
                points.append(str([startX, y]))
        elif startY == endY:
            for x in range(endX if startX > endX else startX, (startX if startX > endX else endX)+1):
                points.append(str([x, startY]))
        else:
            if startX < endX and startY < endY:
                for ii in range(0, abs(startX - endX)+1):
                    points.append(str([startX+ii, startY+ii]))
            elif startX < endX and startY > endY:
                for ii in range(0, abs(startX - endX)+1):
                    points.append(str([startX+ii, startY-ii]))
            elif startX > endX and startY < endY:
                for ii in range(0, abs(startX - endX)+1):
                    points.append(str([startX-ii, startY+ii]))
            elif startX > endX and startY > endY:
                for ii in range(0, abs(startX - endX)+1):
                    points.append(str([startX-ii, startY-ii]))

        #print(line)
        #print(points)

    pointsCount = Counter(points)
    overlaps = 0
    for key in pointsCount:
        if pointsCount[key] > 1:
            overlaps += 1
    print(overlaps)

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)
