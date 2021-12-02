from readFile import readFile

inputLines = readFile("input.txt")

pos = 0
depth = 0

for line in inputLines:
    action, dist = line.split()
    match action:
        case 'forward':
            pos += int(dist)
        case 'up':
            depth -= int(dist)
        case 'down':
            depth += int(dist)

print("Depth: "+str(depth))
print("Pos: "+str(pos))
print("Depth*Pos: "+str(depth*pos))
