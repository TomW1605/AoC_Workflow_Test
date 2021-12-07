from collections import Counter
from tqdm import tqdm

#from readFile import readFile

def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output

def part1(input_lines, days):
    #print(input_lines)
    fish = [int(item) for item in input_lines[0].split(",")]
    for day in tqdm(range(days), unit="day"):
        for ii in tqdm(range(len(fish)), leave=False, unit="fish", unit_scale=True):
            if fish[ii] == 0:
                fish[ii] = 6
                fish.append(8)
            else:
                fish[ii] -= 1
        #print("\r")
        #print("After", day, "days:", len(fish), "fish")# -", fish)
    print("After", days, "days:", len(fish), "fish")# -", fish)

def part2(input_lines, days):
    #print(input_lines)
    fishAges = Counter([int(item) for item in input_lines[0].split(",")])
    print(fishAges)
    for day in range(0, days):
        fishAges[9] = fishAges[0]
        fishAges[0] = fishAges[1]
        fishAges[1] = fishAges[2]
        fishAges[2] = fishAges[3]
        fishAges[3] = fishAges[4]
        fishAges[4] = fishAges[5]
        fishAges[5] = fishAges[6]
        fishAges[6] = fishAges[7] + fishAges[9]
        fishAges[7] = fishAges[8]
        fishAges[8] = fishAges[9]
        fishAges[9] = 0

        total = 0
        for age in fishAges.keys():
            total += fishAges[age]
        print("After", day, "days:", total, "fish")

if __name__ == '__main__':
    test = 0
    part = 1
    days = 256

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines, days)
    elif part == 2:
        part2(inputLines, days)

