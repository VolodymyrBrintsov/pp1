table = []

with open('C:/Users/1/Desktop/pp1/03-FileHandling/universities.txt', 'r') as file:
    for line in file:
        table.append(line)
        
table.sort()
for x in table:
    print(x, end='')