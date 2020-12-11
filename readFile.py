def readFile(file):
    output = []
    f = open(file, "r")
    for x in f:
        output.append(x.strip())
    return output
