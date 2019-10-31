import re
suma = []
with open('C:/Users/1/Desktop/pp1/03-FileHandling/land.txt', 'r') as file:
    kek = re.findall('\d', file.read())
    for i in kek:
        suma.append(int(i))
print(sum(suma))