import json

with open("bro.json", "r") as f:
    bros = json.load(f)

bros['name3'] = {'3': "852"}

for dict in bros.values():
    for value in dict.values():
        print(value)

with open('bro.json', "w") as f:
    json.dump(bros, f)