from urllib.request import urlopen
import pickle
dink = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

for line in dink:
    print(''.join(i * j for i, j in line))