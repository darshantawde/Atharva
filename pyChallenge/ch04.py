import urllib.request
import re

num = '8022'
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
pattern = re.compile("and the next nothing is (\d+)")

while True: 
    yee = urllib.request.urlopen(uri % num).read().decode()
    print(yee)
    match = pattern.search(yee)
    if match == None:
        break
    num = match.group(1)