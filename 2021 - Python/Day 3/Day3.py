from readFile import readFile

def part1(input_lines):
    print(input_lines)
    ones = [0] * len(input_lines[0])
    zeros = [0] * len(input_lines[0])
    for line in input_lines:
        for ii in range(0, len(line)):
            if line[ii] == '1':
                ones[ii] += 1
            elif line[ii] == '0':
                zeros[ii] += 1

    gammaList = ['0'] * len(ones)
    for jj in range(0, len(ones)):
        if ones[jj] > zeros[jj]:
            gammaList[jj] = '1'

    gamma = int(''.join(gammaList), 2)
    epsilon = int(''.join(['1'] * len(gammaList)), 2) - int(''.join(gammaList), 2)
    print(gamma)
    print(epsilon)
    print(gamma*epsilon)


def part2(input_lines):
    print(input_lines)
    o2 = input_lines.copy()
    co2 = input_lines.copy()

    for ii in range(0, len(input_lines[0])):
        if len(o2) == 1:
            break

        ones = 0
        zeros = 0
        o2New = []

        for line in o2:
            if line[ii] == '1':
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            for line in o2:
                if line[ii] == '1':
                    o2New.append(line)
        elif ones < zeros:
            for line in o2:
                if line[ii] == '0':
                    o2New.append(line)
        else:
            for line in o2:
                if line[ii] == '1':
                    o2New.append(line)

        o2 = o2New.copy()

        print(o2)

    for ii in range(0, len(input_lines[0])):
        if len(co2) == 1:
            break

        ones = 0
        zeros = 0
        co2New = []

        for line in co2:
            if line[ii] == '1':
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            for line in co2:
                if line[ii] == '0':
                    co2New.append(line)
        elif ones < zeros:
            for line in co2:
                if line[ii] == '1':
                    co2New.append(line)
        else:
            for line in co2:
                if line[ii] == '0':
                    co2New.append(line)

        co2 = co2New.copy()

        print(co2)

    print(int(o2[0], 2) * int(co2[0], 2))


if __name__ == '__main__':
    inputLines = readFile("input.txt")
    #part1(inputLines)
    part2(inputLines)
