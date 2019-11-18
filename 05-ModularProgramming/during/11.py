import re
file = open('../kek.txt', 'r')
for line in file:
    x = re.findall('\d*', line)
    