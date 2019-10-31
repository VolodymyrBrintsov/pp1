number = []
even = []
file = open('C:/Users/1/Desktop/pp1/03-FileHandling/numbers.txt', 'r')
for line in file:
    number.append(int(line))
for liczba in number:
    if liczba %2 == 0:
        even.append(liczba)
with open('C:/Users/1/Desktop/pp1/03-FileHandling/afterclass/evennumber.txt', 'w')as file:
    for x in even:
        file.write('{}\n'.format(str(x)))
file.close()