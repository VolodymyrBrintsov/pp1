x = int(input('Podaj liczbe: '))
rows = []
while x != 0:
    print(x)
    rows.append(x)
    x = int(input('Podaj liczbe: '))
print('REZULTAT: Liczb:',len(rows),'Suma:',sum(rows),'Srednia:',sum(rows)/len(rows))
    