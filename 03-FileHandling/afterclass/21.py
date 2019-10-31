numbers = []
suma = []
with open('C:/Users/1/Desktop/pp1/03-FileHandling/numbersinrows.txt', 'r')as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(',')
        for liczba in line:
            numbers.append(liczba)
for cyfra in numbers:
    suma.append(int(cyfra))
print(f'Ilosc liczb = {len(numbers)}, a ich suma = {sum(suma)}')