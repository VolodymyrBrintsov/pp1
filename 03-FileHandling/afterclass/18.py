cyfry = []
with open('C:/Users/1/Desktop/pp1/03-FileHandling/numbers.txt', 'r')as file:
    for line in file:
        cyfry.append(int(line))
print(sorted(cyfry))
file.close()