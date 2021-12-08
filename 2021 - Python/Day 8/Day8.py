import re

from readFile import readFile

def part1(input_lines):
    print(input_lines)
    patterns = []
    outputValues = []
    for line in input_lines:
        pattern, outputValue = line.split(" | ")
        patterns.append(pattern)
        outputValues.extend(outputValue.split())
    print(outputValues)

    count = 0
    for value in outputValues:
        if len(value) in [2, 4, 3, 7]:
            count += 1
    print(count)

def subtractSegments(patterns, digit):
    newPatterns = []
    for pattern in patterns:
        newPatterns.append(re.compile("["+"|".join(list(digit))+"]").sub('', pattern))
    return newPatterns

def part2(input_lines):
    print(input_lines)

    total = 0
    for line in input_lines:
        patterns, outputValue = line.split(" | ")
        patterns = patterns.split(" ")
        numbers = {}
        remainingPatterns = []
        for pattern in patterns:
            match len(pattern):
                case 2:
                    numbers[1] = "".join(sorted(list(pattern)))
                case 4:
                    numbers[4] = "".join(sorted(list(pattern)))
                case 3:
                    numbers[7] = "".join(sorted(list(pattern)))
                case 7:
                    numbers[8] = "".join(sorted(list(pattern)))
                case _:
                    remainingPatterns.append("".join(sorted(list(pattern))))
        patterns = remainingPatterns.copy()
        remainingPatterns = []

        patternDict = dict(zip(patterns, subtractSegments(patterns, numbers[7])))

        for pattern in patternDict.keys():
            match len(patternDict[pattern]):
                case 2:
                    numbers[3] = pattern
                case 4:
                    numbers[6] = pattern
                case _:
                    remainingPatterns.append(pattern)
        patterns = remainingPatterns.copy()
        remainingPatterns = []

        patternDict = dict(zip(patterns, subtractSegments(patterns, numbers[6])))

        for pattern in patternDict.keys():
            if len(patternDict[pattern]) == 0:
                numbers[5] = pattern
            else:
                remainingPatterns.append(pattern)
        patterns = remainingPatterns.copy()
        remainingPatterns = []

        patternDict = dict(zip(patterns, subtractSegments(patterns, numbers[3])))

        for pattern in patternDict.keys():
            if len(patternDict[pattern]) == 2:
                numbers[0] = pattern
            else:
                remainingPatterns.append(pattern)
        patterns = remainingPatterns.copy()
        remainingPatterns = []

        for pattern in patterns:
            match len(pattern):
                case 5:
                    numbers[2] = pattern
                case 6:
                    numbers[9] = pattern
                case _:
                    remainingPatterns.append(pattern)
        patterns = remainingPatterns.copy()
        remainingPatterns = []

        print(numbers)

        mapping = {v: k for k, v in numbers.items()}

        number = ""
        for digit in outputValue.split(" "):
            number += str(mapping["".join(sorted(list(digit)))])
        total += int(number)

    print(total)

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

