from readFile import readFile

def part1(input_lines):
    #print(input_lines)
    crabs = [int(item) for item in input_lines[0].split(",")]
    totalCosts = []
    for loc in range(min(crabs), max(crabs)+1):
        #print(loc)
        totalCost = 0
        for crab in crabs:
            totalCost += abs(crab - loc)
        totalCosts.append(totalCost)
        print(loc, "-", totalCost)
    print(totalCosts)
    print(min(totalCosts))

def part2(input_lines):
    #print(input_lines)
    crabs = [int(item) for item in input_lines[0].split(",")]
    totalCosts = []
    for loc in range(min(crabs), max(crabs) + 1):
        #print(loc)
        totalCost = 0
        for crab in crabs:
            distance = abs(crab - loc)
            totalCost += int((distance*(distance+1))/2)
        totalCosts.append(totalCost)
        print(loc, "-", totalCost)
    #print(totalCosts)
    print(min(totalCosts))

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

