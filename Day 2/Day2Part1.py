from readFile import readFile

inputLines = readFile("Day2.txt")

numValid = 0

for line in inputLines:
    nums, letter, password = line.split(" ")
    minTimes, maxTimes = nums.split("-")
    minTimes = int(minTimes)
    maxTimes = int(maxTimes)
    letter = letter.strip(":")
    numIn = 0
    for char in password:
        if char == letter:
            numIn += 1
    if minTimes <= numIn and numIn <= maxTimes:
        numValid += 1

print(numValid)
