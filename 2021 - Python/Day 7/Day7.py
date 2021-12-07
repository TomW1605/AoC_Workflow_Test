from readFile import readFile

def part1(input_lines):
    #print(input_lines)
    crabs = [int(item) for item in input_lines[0].split(",")]
    minFuel = 0
    dest = 0
    for loc in range(min(crabs), max(crabs)+1):
        #print(loc)
        totalFuel = 0
        for crab in crabs:
            totalFuel += abs(crab - loc)

        if totalFuel < minFuel or minFuel == 0:
            minFuel = totalFuel
            dest = loc
        else:
            break
        print(loc, "-", totalFuel)
    print("cheapest dest:", dest, "-", minFuel)

def part2(input_lines):
    #print(input_lines)
    crabs = [int(item) for item in input_lines[0].split(",")]
    minFuel = 0
    dest = 0
    for loc in range(min(crabs), max(crabs) + 1):
        #print(loc)
        totalFuel = 0
        for crab in crabs:
            distance = abs(crab - loc)
            totalFuel += int((distance*(distance+1))/2)

        if totalFuel < minFuel or minFuel == 0:
            minFuel = totalFuel
            dest = loc
        else:
            break
        print(loc, "-", totalFuel)
    print("cheapest dest:", dest, "-", minFuel)

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

