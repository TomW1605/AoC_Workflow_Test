from readFile import readFile

inputLines = readFile("Day4.txt")

passports = []
passport = ""
validNum = 0

reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

for line in inputLines:
    if line != "":
        passport = passport + " " + line
    else:
        passports.append(passport.strip())
        passport = ""

print(passports)

for passport in passports:
    fields = passport.split(" ")
    for ii in range(0, len(fields)):
        fields[ii] = fields[ii].split(":")[0]
    missing = [item for item in reqFields if item not in fields]
    if missing == [] or missing == ['cid']:
        validNum += 1

print(validNum)
