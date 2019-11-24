import csv
import re
with open('../employees.csv', newline='') as f:
    linia=0
    age = []
    reader = csv.reader(f)

    for row in reader:
            if linia==0:
                print('#', *row)
                linia+=1
            else:    
                print(f' {linia}',end=' ')
                print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
                linia+=1