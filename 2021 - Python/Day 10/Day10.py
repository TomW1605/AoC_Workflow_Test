from readFile import readFile

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
charMap = dict(zip(openers, closers))
errorValues = {')': 3, ']': 57, '}': 1197, '>': 25137}
fixValues = {')': 1, ']': 2, '}': 3, '>': 4}

def part1(input_lines):
    #print(input_lines)
    errorScore = 0
    incompleteLines = input_lines.copy()
    for line in input_lines:
        lineStack = []
        for char in line:
            if char in openers:
                lineStack.append(char)
            elif char in closers:
                opener = lineStack.pop()
                if char != charMap[opener]:
                    errorScore += errorValues[char]
                    incompleteLines.remove(line)
                    break
    print(errorScore)
    return incompleteLines

def part2(input_lines):
    #print(input_lines)
    incompleteLines = part1(input_lines)
    fixScores = []
    for line in incompleteLines:
        lineStack = []
        lineFixScore = 0
        for char in line:
            if char in openers:
                lineStack.append(char)
            elif char in closers:
                lineStack.pop()
        for opener in reversed(lineStack):
            lineFixScore *= 5
            lineFixScore += fixValues[charMap[opener]]
        fixScores.append(lineFixScore)
    fixScore = sorted(fixScores)[int((len(fixScores) - 1)/2)]
    print(fixScore)

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

