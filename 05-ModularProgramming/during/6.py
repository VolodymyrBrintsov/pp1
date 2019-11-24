import csv
import re
with open('../employees.csv', newline='') as f:
    linia=0
    age = []
    reader = csv.reader(f)    
    for row in reader:
        wiek = re.findall('\d+',row[2])
        for x in wiek:
            age.append(int(x))
    print(sum(age)/len(age))
    