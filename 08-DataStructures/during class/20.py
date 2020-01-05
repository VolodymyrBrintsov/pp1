import json
komp = {
    "nazwa": "Lenovo",
    "procesor": "IntelCore i9",
    "monitor": 17,
    "czesto uzywane pliki": ['Ulubione gry', 'Muzyka'],
    "oficjalny windows": True,
    }

with open("komputer.json", "w")as file:
    json.dump(komp, file, indent=4)

with open("komputer.json")as file:
    data = json.load(file)
    
print(data['czesto uzywane pliki'][0])
    
