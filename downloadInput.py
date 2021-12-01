import configparser

import requests as requests

config = configparser.ConfigParser()
config.read('/config.ini')

cookies_dict = {"session": config["sessionID"]}
response = requests.get("https://adventofcode.com/2021/day/1/input", cookies=cookies_dict)

print(response.content)
