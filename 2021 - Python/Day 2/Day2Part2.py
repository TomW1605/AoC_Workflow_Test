from readFile import readFile

inputLines = readFile("input.txt")

pos = 0
depth = 0
aim = 0

for line in inputLines:
    action, dist = line.split()
    match action:
        case 'forward':
            pos += int(dist)
            depth += aim*int(dist)
        case 'up':
            aim -= int(dist)
        case 'down':
            aim += int(dist)

print("Depth: "+str(depth))
print("Pos: "+str(pos))
print("Depth*Pos: "+str(depth*pos))
