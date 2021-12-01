import configparser
import os

import requests as requests

config = configparser.ConfigParser()
config.read('config.ini')

folder = config['general']['year'] + " - " + config['general']['language']

completedDays = next(os.walk(os.path.join('.', folder)))[1]
completedDays.sort()
if len(completedDays) > 0:
    dayNum = int(completedDays[-1].split(" ")[-1]) + 1
else:
    dayNum = 1

if dayNum > 25:
    print("There are only 25 challenges in "+config['general']['year']+". Make sure the year is right in config.ini")
    exit(1)

os.mkdir(os.path.join(folder, "Day "+str(dayNum)))

response = requests.get("https://adventofcode.com/"+config['general']['year']+"/day/"+str(dayNum)+"/input", cookies={"session": config['general']['sessionID']})
with open(os.path.join(folder, "Day "+str(dayNum), "input.txt"), "w") as inputFile:
    inputFile.write(response.text)

with open(os.path.join(folder, "Day "+str(dayNum), "Day"+str(dayNum)+"Part1."+config['general']['extension']), 'w') as part1File:
    part1File.write(config['general']['prefill']+'\n')

with open(os.path.join(folder, "Day "+str(dayNum), "Day"+str(dayNum)+"Part2."+config['general']['extension']), 'w') as part2File:
    part2File.write(config['general']['prefill']+'\n')
