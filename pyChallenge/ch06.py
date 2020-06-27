import re

FILE = 'channel/%s.txt'
num = '90052'
pattern = re.compile("Next nothing is (\d+)")

while True: 
    yee = open(FILE % num, 'r')
    for line in yee:
        print(line)

    match = pattern.search(line)
    if match == None:
        break
    num = match.group(1)