import math

from readFile import readFile

def part1(input_lines):
    #print(input_lines)

    width = len(input_lines[0])
    height = len(input_lines)

    grid = [[math.inf]*(width+2)] + [[math.inf]+[int(point) for point in list(line)]+[math.inf] for line in input_lines] + [[math.inf]*(width+2)]
    #print(grid)
    totalRisk = 0
    lowPoints = []
    for row in range(1, height+1):
        for col in range(1, width+1):
            point = int(grid[row][col])
            #print(point)
            if point < grid[row+1][col] and point < grid[row-1][col] and point < grid[row][col+1] and point < grid[row][col-1]:
                totalRisk += point + 1
                #print("point")
                lowPoints.append([row, col])
    print(totalRisk)
    return lowPoints

def surroundingPoints(grid, row, col, countedPoints: list[list[int]]):
    searchList = [[grid[row+1][col], [row+1, col]], [grid[row-1][col], [row-1, col]], [grid[row][col+1], [row, col+1]], [grid[row][col-1], [row, col-1]]]
    for point in searchList:
        if point[0] > grid[row][col] and point[0] != 9 and [point[1][0], point[1][1]] not in countedPoints:
            countedPoints.append([point[1][0], point[1][1]])
            countedPoints = surroundingPoints(grid, point[1][0], point[1][1], countedPoints)
    return countedPoints

def part2(input_lines):
    print(input_lines)
    lowPoints = part1(input_lines)
    width = len(input_lines[0])
    height = len(input_lines)
    grid = [[9]*(width+2)]+[[9]+[int(point) for point in list(line)]+[9] for line in input_lines]+[[9]*(width+2)]
    basins = []
    for lowPoint in lowPoints:
        countedPoints = surroundingPoints(grid, lowPoint[0], lowPoint[1], [])
        basins.append(len(countedPoints)+1)

    totalSize = 1
    for size in list(reversed(sorted(basins)))[0:3]:
        totalSize *= size
    print(totalSize)

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

