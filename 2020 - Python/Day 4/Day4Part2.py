import re

from readFile import readFile

inputLines = readFile("Day4.txt")

passports = []
passport = ""
validNum = 0

reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for line in inputLines:
    if line != "":
        passport = passport+" "+line
    else:
        passports.append(passport.strip())
        passport = ""

#print(passports)

for passport in passports:
    fields = passport.split(" ")
    data = {}
    for field in fields:
        data.update({field.split(":")[0]: field.split(":")[1]})
    try:
        if len(data["byr"]) == 4 and 1920 <= int(data["byr"]) <= 2002:
            if len(data["iyr"]) == 4 and 2010 <= int(data["iyr"]) <= 2020:
                if len(data["eyr"]) == 4 and 2020 <= int(data["eyr"]) <= 2030:
                    if (data["hgt"][-2:] == "cm" and 150 <= int(data["hgt"][:-2]) <= 193) or \
                            (data["hgt"][-2:] == "in" and 59 <= int(data["hgt"][:-2]) <= 76):
                            if bool(re.match("^#([a-fA-F0-9]{6})$", data["hcl"])):
                                if data["ecl"] in ecl:
                                    if re.match("^([0-9]{9})$", data["pid"]):
                                        validNum += 1
    except KeyError:
        continue

print(validNum)
