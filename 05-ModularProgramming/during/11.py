import re
file = open('Wydatki.txt', 'r')
for line in file:
    liczby = re.findall('\d',line)
print(liczby)
    