import json
with open("euro.json") as file:
    data = json.load(file)
kek = '''Data\t\tKupno\t\tSprzedaz
========================================\n'''    
for k in range(len(data['rates'])):
    kek += f"{data['rates'][k]['effectiveDate']}\t{data['rates'][k]['bid']}\t\t{data['rates'][k]['ask']}\n"
print(kek)