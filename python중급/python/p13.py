import json

li = [{'name': 'Eric', 'kor': 77, 'eng': 90, 'math': 70},
      {'name': 'John', 'kor': 87, 'eng': 82, 'math': 84},
      {'name': 'Jay', 'kor': 90, 'eng': 85, 'math': 74},]

with open('/Users/JuneHyukLee/Desktop/abc.json', 'w') as f:
    json.dump(li, f)