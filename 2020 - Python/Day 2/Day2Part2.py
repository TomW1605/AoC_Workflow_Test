from readFile import readFile

inputLines = readFile("Day2.txt")

numValid = 0

for line in inputLines:
    nums, letter, password = line.split(" ")
    pos1, pos2 = nums.split("-")
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    letter = letter.strip(":")
    if (password[pos1] == letter and password[pos2] != letter) or (password[pos1] != letter and password[pos2] == letter):
        numValid += 1

print(numValid)
