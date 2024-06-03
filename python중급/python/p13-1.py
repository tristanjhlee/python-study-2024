import json

with open('/Users/JuneHyukLee/Desktop/abc.json', 'r') as f:
    info = json.load(f)

for i in info:
    for k,v in i.items(): # k: Key, v: Value
        print(k,v)
    print('-' * 30)